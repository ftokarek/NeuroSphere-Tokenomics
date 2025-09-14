#!/usr/bin/env python3
"""
NeuroSphere Tokenomics Financial Model
Comprehensive analysis and Monte Carlo simulation for crypto investor presentation
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

class NeuroSphereModel:
    """
    Comprehensive financial and tokenomics model for NeuroSphere platform
    """
    
    def __init__(self):
        # Platform Parameters
        self.trading_fee_rate = 0.002  # 0.2% trading fee
        self.nst_fee_share = 0.30      # 30% of fees to NST stakers
        
        # Market assumptions based on pump.fun data
        self.pump_fun_peak_volume = 3_000_000_000  # $3B daily at peak
        self.pump_fun_current_volume = 170_000_000  # $170M current daily
        
        # AI API costs (from pricing data)
        self.ai_api_costs = {
            'gpt_4_turbo': 0.03,     # per 1k tokens
            'gpt_3_5_turbo': 0.002,  # per 1k tokens
            'dalle_3': 0.02,         # per image
            'whisper': 0.006,        # per minute
        }
        
        # Operating cost assumptions
        self.annual_costs = {
            'development': 500_000,
            'marketing': 300_000,
            'operations': 200_000,
            'infrastructure': 100_000,
            'legal_compliance': 50_000
        }
        
    def calculate_market_scenarios(self):
        """Calculate trading volume scenarios based on market penetration"""
        scenarios = {
            'conservative': {
                'pump_fun_share': 0.001,  # 0.1% of pump.fun
                'daily_volume_multiplier': 0.5,  # Based on current not peak
                'growth_rate': 0.02,  # 2% monthly growth
                'description': 'Conservative adoption with 0.1% pump.fun share'
            },
            'base_case': {
                'pump_fun_share': 0.005,  # 0.5% of pump.fun
                'daily_volume_multiplier': 0.7,
                'growth_rate': 0.05,  # 5% monthly growth
                'description': 'Realistic adoption with 0.5% pump.fun share'
            },
            'optimistic': {
                'pump_fun_share': 0.02,   # 2% of pump.fun
                'daily_volume_multiplier': 1.0,  # Peak market conditions
                'growth_rate': 0.10,  # 10% monthly growth
                'description': 'Strong adoption with 2% pump.fun share'
            },
            'moonshot': {
                'pump_fun_share': 0.10,   # 10% of pump.fun
                'daily_volume_multiplier': 1.5,  # Exceeds pump.fun peak
                'growth_rate': 0.15,  # 15% monthly growth
                'description': 'Exceptional success scenario'
            }
        }
        
        for scenario_name, params in scenarios.items():
            base_daily_volume = (self.pump_fun_current_volume * 
                               params['daily_volume_multiplier'] * 
                               params['pump_fun_share'])
            scenarios[scenario_name]['initial_daily_volume'] = base_daily_volume
            scenarios[scenario_name]['initial_annual_volume'] = base_daily_volume * 365
            scenarios[scenario_name]['initial_annual_revenue'] = (
                base_daily_volume * 365 * self.trading_fee_rate
            )
        
        return scenarios
    
    def monte_carlo_simulation(self, scenario_params, num_simulations=10000, years=5):
        """Run Monte Carlo simulation for revenue projections"""
        results = []
        
        for sim in range(num_simulations):
            # Random variables with distributions
            market_penetration = np.random.beta(2, 5) * scenario_params['pump_fun_share'] * 2
            volume_multiplier = np.random.lognormal(
                np.log(scenario_params['daily_volume_multiplier']), 0.3
            )
            growth_volatility = np.random.normal(0, 0.02)
            
            # Calculate base volume
            base_volume = (self.pump_fun_current_volume * 
                          volume_multiplier * market_penetration)
            
            yearly_revenues = []
            current_volume = base_volume
            
            for year in range(years):
                # Apply growth with volatility
                growth_rate = scenario_params['growth_rate'] + growth_volatility
                if year > 0:
                    current_volume *= (1 + growth_rate) ** 12
                
                # Add market cycle volatility
                market_cycle = np.random.normal(1, 0.2)
                adjusted_volume = current_volume * market_cycle
                
                annual_revenue = adjusted_volume * 365 * self.trading_fee_rate
                yearly_revenues.append(max(0, annual_revenue))  # No negative revenues
            
            results.append(yearly_revenues)
        
        return np.array(results)
    
    def calculate_token_economics(self, daily_volume, daily_active_users=1000):
        """Model prompt token and NST economics"""
        
        # Prompt token assumptions
        avg_prompts_per_user = 5
        prompt_utilization_rate = 0.1  # 10% of owned tokens burned monthly
        avg_prompt_token_price = 0.1   # $0.10 per token
        
        # Calculate prompt token metrics
        daily_prompt_creation = daily_active_users * 0.1  # 10% create prompts daily
        daily_prompt_tokens_minted = daily_prompt_creation * 1000  # 1000 tokens per prompt
        
        # Trading volume breakdown
        prompt_trading_volume = daily_volume * 0.8  # 80% from prompt tokens
        nst_trading_volume = daily_volume * 0.2     # 20% from NST
        
        # Burn mechanics
        monthly_burns = daily_active_users * avg_prompts_per_user * prompt_utilization_rate
        daily_burns = monthly_burns / 30
        
        # NST value accrual
        daily_trading_fees = daily_volume * self.trading_fee_rate
        daily_nst_rewards = daily_trading_fees * self.nst_fee_share
        
        return {
            'daily_prompt_creation': daily_prompt_creation,
            'daily_tokens_minted': daily_prompt_tokens_minted,
            'daily_tokens_burned': daily_burns,
            'net_token_supply_change': daily_prompt_tokens_minted - daily_burns,
            'daily_nst_rewards': daily_nst_rewards,
            'annual_nst_rewards': daily_nst_rewards * 365,
            'prompt_trading_volume': prompt_trading_volume,
            'nst_trading_volume': nst_trading_volume
        }
    
    def break_even_analysis(self):
        """Calculate break-even metrics"""
        total_annual_costs = sum(self.annual_costs.values())
        
        break_even_annual_revenue = total_annual_costs
        break_even_annual_volume = break_even_annual_revenue / self.trading_fee_rate
        break_even_daily_volume = break_even_annual_volume / 365
        
        # User metrics for break-even
        # Assuming average user generates $10 trading volume per day
        avg_user_daily_volume = 10
        break_even_daily_users = break_even_daily_volume / avg_user_daily_volume
        
        return {
            'total_annual_costs': total_annual_costs,
            'break_even_annual_revenue': break_even_annual_revenue,
            'break_even_annual_volume': break_even_annual_volume,
            'break_even_daily_volume': break_even_daily_volume,
            'break_even_daily_users': break_even_daily_users
        }
    
    def sensitivity_analysis(self):
        """Analyze sensitivity to key parameters"""
        base_case = self.calculate_market_scenarios()['base_case']
        base_revenue = base_case['initial_annual_revenue']
        
        sensitivities = {}
        
        # Trading fee sensitivity
        fee_rates = np.linspace(0.001, 0.005, 10)  # 0.1% to 0.5%
        fee_revenues = [base_case['initial_annual_volume'] * rate for rate in fee_rates]
        sensitivities['trading_fee'] = {
            'rates': fee_rates,
            'revenues': fee_revenues,
            'elasticity': np.diff(fee_revenues) / np.diff(fee_rates) / base_revenue
        }
        
        # Market penetration sensitivity
        penetrations = np.linspace(0.001, 0.02, 10)
        penetration_revenues = [
            self.pump_fun_current_volume * 365 * p * self.trading_fee_rate 
            for p in penetrations
        ]
        sensitivities['market_penetration'] = {
            'penetrations': penetrations,
            'revenues': penetration_revenues
        }
        
        # User growth sensitivity
        growth_rates = np.linspace(0.01, 0.15, 10)
        growth_revenues = []
        for growth in growth_rates:
            year_1_volume = base_case['initial_daily_volume'] * 365 * (1 + growth)**6
            growth_revenues.append(year_1_volume * self.trading_fee_rate)
        sensitivities['growth_rate'] = {
            'rates': growth_rates,
            'revenues': growth_revenues
        }
        
        return sensitivities
    
    def competitive_analysis(self):
        """Analyze competitive positioning vs other platforms"""
        competitors = {
            'pump_fun': {
                'trading_fee': 0.01,  # 1% (estimated)
                'utility': 'Low - speculative trading only',
                'revenue_model': 'Trading fees only',
                'token_supply': 'Fixed supply, no burn',
                'market_cap_range': (1_000_000, 1_000_000_000)
            },
            'promptbase': {
                'trading_fee': 0.20,  # 20% commission
                'utility': 'High - AI prompt marketplace',
                'revenue_model': 'Commission on sales',
                'token_supply': 'No tokenization',
                'market_cap_range': None
            },
            'neurosphere': {
                'trading_fee': 0.002,  # 0.2%
                'utility': 'High - functional AI prompts + trading',
                'revenue_model': 'Trading fees + burn mechanism',
                'token_supply': 'Dynamic supply with burn',
                'projected_market_cap': (10_000_000, 100_000_000)
            }
        }
        
        return competitors
    
    def create_financial_dashboard(self):
        """Create comprehensive financial visualization dashboard"""
        scenarios = self.calculate_market_scenarios()
        
        # Create subplots
        fig = make_subplots(
            rows=3, cols=2,
            subplot_titles=[
                'Revenue Projections by Scenario',
                'Market Penetration vs Revenue',
                'Break-Even Analysis',
                'Token Economics',
                'Sensitivity Analysis',
                'Competitive Positioning'
            ],
            specs=[
                [{"secondary_y": False}, {"secondary_y": False}],
                [{"secondary_y": False}, {"secondary_y": False}],
                [{"secondary_y": False}, {"secondary_y": False}]
            ]
        )
        
        # Revenue projections
        years = list(range(1, 6))
        for scenario_name, params in scenarios.items():
            revenues = []
            current_revenue = params['initial_annual_revenue']
            for year in years:
                if year == 1:
                    revenues.append(current_revenue)
                else:
                    current_revenue *= (1 + params['growth_rate']) ** 12
                    revenues.append(current_revenue)
            
            fig.add_trace(
                go.Scatter(
                    x=years, y=revenues, name=scenario_name.title(),
                    mode='lines+markers'
                ),
                row=1, col=1
            )
        
        # Break-even analysis
        break_even = self.break_even_analysis()
        costs = list(self.annual_costs.values())
        cost_labels = list(self.annual_costs.keys())
        
        fig.add_trace(
            go.Bar(x=cost_labels, y=costs, name='Annual Costs'),
            row=2, col=1
        )
        
        return fig

def main():
    """Main analysis execution"""
    print("🚀 NeuroSphere Tokenomics Analysis")
    print("=" * 50)
    
    model = NeuroSphereModel()
    
    # Calculate scenarios
    scenarios = model.calculate_market_scenarios()
    print("\n📊 Market Scenarios:")
    for name, params in scenarios.items():
        print(f"\n{name.upper()}:")
        print(f"  Initial Daily Volume: ${params['initial_daily_volume']:,.0f}")
        print(f"  Initial Annual Revenue: ${params['initial_annual_revenue']:,.0f}")
        print(f"  Description: {params['description']}")
    
    # Break-even analysis
    break_even = model.break_even_analysis()
    print(f"\n💰 Break-Even Analysis:")
    print(f"  Total Annual Costs: ${break_even['total_annual_costs']:,.0f}")
    print(f"  Break-Even Daily Volume: ${break_even['break_even_daily_volume']:,.0f}")
    print(f"  Break-Even Daily Users: {break_even['break_even_daily_users']:,.0f}")
    
    # Monte Carlo simulation for base case
    print(f"\n🎲 Monte Carlo Simulation (Base Case):")
    base_case = scenarios['base_case']
    mc_results = model.monte_carlo_simulation(base_case)
    
    # Calculate percentiles for Year 1
    year_1_revenues = mc_results[:, 0]
    percentiles = [10, 25, 50, 75, 90]
    print(f"  Year 1 Revenue Percentiles:")
    for p in percentiles:
        value = np.percentile(year_1_revenues, p)
        print(f"    {p}th percentile: ${value:,.0f}")
    
    # Token economics
    base_volume = base_case['initial_daily_volume']
    token_metrics = model.calculate_token_economics(base_volume)
    print(f"\n🪙 Token Economics (Base Case):")
    print(f"  Daily Prompt Creation: {token_metrics['daily_prompt_creation']:,.0f}")
    print(f"  Daily Tokens Burned: {token_metrics['daily_tokens_burned']:,.0f}")
    print(f"  Annual NST Rewards: ${token_metrics['annual_nst_rewards']:,.0f}")
    
    # Sensitivity analysis
    sensitivities = model.sensitivity_analysis()
    print(f"\n📈 Key Sensitivities:")
    print(f"  Trading fee elasticity (avg): {np.mean(sensitivities['trading_fee']['elasticity']):.2f}")
    
    # Competitive analysis
    competitors = model.competitive_analysis()
    print(f"\n🏆 Competitive Advantages:")
    print(f"  NeuroSphere fee: {competitors['neurosphere']['trading_fee']*100:.1f}%")
    print(f"  Pump.fun fee: {competitors['pump_fun']['trading_fee']*100:.1f}%")
    print(f"  PromptBase fee: {competitors['promptbase']['trading_fee']*100:.1f}%")
    
    print(f"\n✅ Analysis Complete!")
    return model

if __name__ == "__main__":
    model = main()
