#!/usr/bin/env python3
"""
NeuroSphere Business Case Generator
Creates investor-ready charts and key metrics for September 17, 2025 pitch
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.patches import Rectangle
import warnings
warnings.filterwarnings('ignore')

# Set style for professional charts
plt.style.use('default')
sns.set_palette("husl")

class BusinessCaseCharts:
    """Generate professional charts for investor presentation"""
    
    def __init__(self):
        self.pumpfun_daily_volume = 170_000_000  # €170M daily
        self.pumpfun_daily_revenue = 1_700_000   # €1.7M daily (1% fee)
        self.neurosphere_fee = 0.002             # 0.2%
        
    def create_market_opportunity_chart(self):
        """Chart showing market size and NeuroSphere's opportunity"""
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Chart 1: Market Size Comparison
        markets = ['Pump.fun\nCurrent', 'NeuroSphere\n0.5% Share', 'NeuroSphere\n2% Share', 'NeuroSphere\n10% Share']
        volumes = [170_000_000, 850_000, 3_400_000, 17_000_000]
        revenues = [1_700_000, 1_700, 6_800, 34_000]
        
        x_pos = np.arange(len(markets))
        bars1 = ax1.bar(x_pos, volumes, alpha=0.8, color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
        
        ax1.set_xlabel('Market Scenarios', fontsize=12, fontweight='bold')
        ax1.set_ylabel('Daily Volume ($)', fontsize=12, fontweight='bold')
        ax1.set_title('Market Opportunity: Daily Trading Volume', fontsize=14, fontweight='bold')
        ax1.set_xticks(x_pos)
        ax1.set_xticklabels(markets, fontsize=10)
        ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))
        
        # Add value labels on bars
        for i, (bar, volume) in enumerate(zip(bars1, volumes)):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + height*0.05,
                    f'${volume/1e6:.1f}M', ha='center', va='bottom', fontweight='bold', fontsize=12)
        
        # Chart 2: Revenue Comparison
        bars2 = ax2.bar(x_pos, revenues, alpha=0.8, color=['#e74c3c', '#3498db', '#2ecc71', '#f39c12'])
        
        ax2.set_xlabel('Market Scenarios', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Daily Revenue ($)', fontsize=12, fontweight='bold')
        ax2.set_title('Revenue Potential: Daily Platform Revenue', fontsize=14, fontweight='bold')
        ax2.set_xticks(x_pos)
        ax2.set_xticklabels(markets, fontsize=10)
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M' if x >= 1e6 else f'${x/1e3:.0f}K' if x >= 1000 else f'${x:.0f}'))
        
        # Add value labels on bars
        for i, (bar, revenue) in enumerate(zip(bars2, revenues)):
            height = bar.get_height()
            if revenue >= 1e6:
                label = f'${revenue/1e6:.1f}M'
            elif revenue >= 1000:
                label = f'${revenue/1e3:.0f}K'
            else:
                label = f'${revenue:.0f}'
            ax2.text(bar.get_x() + bar.get_width()/2., height + height*0.05,
                    label, ha='center', va='bottom', fontweight='bold', fontsize=12)
        
        plt.tight_layout()
        plt.savefig('market_opportunity.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_competitive_advantage_chart(self):
        """Chart comparing NeuroSphere vs Pump.fun"""
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # Chart 1: Fee Comparison
        platforms = ['Pump.fun', 'NeuroSphere']
        fees = [1.0, 0.2]
        colors = ['#e74c3c', '#2ecc71']
        
        bars1 = ax1.bar(platforms, fees, color=colors, alpha=0.8)
        ax1.set_ylabel('Platform Fee (%)', fontsize=12, fontweight='bold')
        ax1.set_title('Platform Fee Comparison', fontsize=14, fontweight='bold')
        ax1.set_ylim(0, 1.2)
        
        for bar, fee in zip(bars1, fees):
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                    f'{fee}%', ha='center', va='bottom', fontweight='bold', fontsize=12)
        
        # Chart 2: Utility Comparison
        categories = ['Speculation\nOnly', 'Real AI\nUtility', 'Burn\nMechanism', 'Network\nEffects']
        pumpfun_scores = [100, 0, 0, 20]
        neurosphere_scores = [100, 100, 100, 80]
        
        x = np.arange(len(categories))
        width = 0.35
        
        bars1 = ax2.bar(x - width/2, pumpfun_scores, width, label='Pump.fun', color='#e74c3c', alpha=0.7)
        bars2 = ax2.bar(x + width/2, neurosphere_scores, width, label='NeuroSphere', color='#2ecc71', alpha=0.7)
        
        ax2.set_ylabel('Value Score (0-100)', fontsize=12, fontweight='bold')
        ax2.set_title('Platform Value Comparison', fontsize=14, fontweight='bold')
        ax2.set_xticks(x)
        ax2.set_xticklabels(categories, fontsize=10)
        ax2.legend()
        ax2.set_ylim(0, 120)
        
        # Chart 3: Revenue Growth Projection
        years = [2025, 2026, 2027, 2028, 2029]
        conservative = [620_000, 1_240_000, 2_480_000, 4_960_000, 9_920_000]
        realistic = [2_500_000, 8_000_000, 15_700_000, 31_400_000, 62_800_000]
        optimistic = [12_400_000, 39_700_000, 78_500_000, 157_000_000, 314_000_000]
        
        ax3.plot(years, conservative, marker='o', linewidth=3, label='Conservative (0.5%)', color='#3498db')
        ax3.plot(years, realistic, marker='s', linewidth=3, label='Realistic (2%)', color='#2ecc71')
        ax3.plot(years, optimistic, marker='^', linewidth=3, label='Optimistic (10%)', color='#f39c12')
        
        ax3.set_xlabel('Year', fontsize=12, fontweight='bold')
        ax3.set_ylabel('Annual Revenue ($)', fontsize=12, fontweight='bold')
        ax3.set_title('5-Year Revenue Projections', fontsize=14, fontweight='bold')
        ax3.legend()
        ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))
        ax3.grid(True, alpha=0.3)
        
        # Chart 4: ROI Timeline
        investment = 500_000  # $500K
        equity = 0.15  # 15%
        
        scenarios = ['Conservative\n(0.5% share)', 'Realistic\n(2% share)', 'Optimistic\n(10% share)']
        year3_valuations = [19_840_000, 125_600_000, 628_000_000]  # 8x revenue multiple
        year5_valuations = [79_360_000, 502_400_000, 2_512_000_000]  # 8x revenue multiple
        
        investor_value_y3 = [val * equity for val in year3_valuations]
        investor_value_y5 = [val * equity for val in year5_valuations]
        
        roi_y3 = [(val - investment) / investment for val in investor_value_y3]
        roi_y5 = [(val - investment) / investment for val in investor_value_y5]
        
        x = np.arange(len(scenarios))
        width = 0.35
        
        bars1 = ax4.bar(x - width/2, roi_y3, width, label='3-Year ROI', color='#9b59b6', alpha=0.7)
        bars2 = ax4.bar(x + width/2, roi_y5, width, label='5-Year ROI', color='#e67e22', alpha=0.7)
        
        ax4.set_ylabel('ROI Multiple (x)', fontsize=12, fontweight='bold')
        ax4.set_title('Investor ROI Projections ($500K Investment)', fontsize=14, fontweight='bold')
        ax4.set_xticks(x)
        ax4.set_xticklabels(scenarios, fontsize=10)
        ax4.legend()
        
        # Add value labels
        for i, (bar1, bar2) in enumerate(zip(bars1, bars2)):
            h1, h2 = bar1.get_height(), bar2.get_height()
            ax4.text(bar1.get_x() + bar1.get_width()/2., h1 + max(h1, h2)*0.02,
                    f'{h1:.0f}x', ha='center', va='bottom', fontweight='bold', fontsize=11)
            ax4.text(bar2.get_x() + bar2.get_width()/2., h2 + max(h1, h2)*0.02,
                    f'{h2:.0f}x', ha='center', va='bottom', fontweight='bold', fontsize=11)
        
        plt.tight_layout()
        plt.savefig('competitive_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_tokenomics_diagram(self):
        """Visual diagram of tokenomics flow"""
        
        fig, ax = plt.subplots(1, 1, figsize=(14, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        # Title
        ax.text(5, 7.5, 'NeuroSphere Tokenomics Flow', fontsize=20, fontweight='bold', ha='center')
        
        # Boxes and flows
        boxes = [
            # (x, y, width, height, text, color)
            (0.5, 5.5, 2, 1, 'User Creates\nAI Prompt', '#3498db'),
            (3.5, 5.5, 2, 1, 'Prompt Tokenized\n1M Supply', '#2ecc71'),
            (6.5, 5.5, 2, 1, 'Trading on\nPlatform', '#f39c12'),
            
            (0.5, 3.5, 2, 1, 'User Burns Token\nto Use Prompt', '#e74c3c'),
            (3.5, 3.5, 2, 1, 'Supply Reduces\nPrice Increases', '#9b59b6'),
            (6.5, 3.5, 2, 1, '0.2% Trading Fee\nGenerated', '#1abc9c'),
            
            (2, 1.5, 2.5, 1, 'NST Stakers Get\n30% of Fees', '#e67e22'),
            (5.5, 1.5, 2.5, 1, 'Platform Revenue\n70% of Fees', '#34495e'),
        ]
        
        for x, y, w, h, text, color in boxes:
            rect = Rectangle((x, y), w, h, facecolor=color, alpha=0.7, edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontweight='bold', fontsize=11)
        
        # Arrows
        arrows = [
            # (start_x, start_y, end_x, end_y)
            (2.5, 6, 3.5, 6),      # Create → Tokenize
            (5.5, 6, 6.5, 6),      # Tokenize → Trade
            (1.5, 5.5, 1.5, 4.5),  # Down to burn
            (4.5, 5.5, 4.5, 4.5),  # Down to supply
            (7.5, 5.5, 7.5, 4.5),  # Down to fees
            (3.25, 3.5, 3.25, 2.5), # To NST
            (6.75, 3.5, 6.75, 2.5), # To platform
        ]
        
        for start_x, start_y, end_x, end_y in arrows:
            ax.annotate('', xy=(end_x, end_y), xytext=(start_x, start_y),
                       arrowprops=dict(arrowstyle='->', lw=2, color='black'))
        
        # Add cycle arrow
        ax.annotate('', xy=(1.5, 5.5), xytext=(7.5, 4.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='red', 
                                 connectionstyle="arc3,rad=0.3"))
        ax.text(4.5, 2.8, 'Value Creation Cycle', ha='center', fontsize=12, 
               fontweight='bold', color='red')
        
        plt.savefig('tokenomics_flow.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_funding_allocation_chart(self):
        """Chart showing fund allocation and timeline"""
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Chart 1: Fund Allocation Pie Chart
        categories = ['Core Team Dev\n40%', 'Infrastructure\n16%', 'Marketing\n16%', 'Buffer\n18%', 'Legal\n6%', 'Launch\n4%']
        sizes = [40, 16, 16, 18, 6, 4]
        colors = ['#3498db', '#f39c12', '#2ecc71', '#9b59b6', '#e74c3c', '#1abc9c']
        amounts = ['$200K', '$80K', '$80K', '$90K', '$30K', '$20K']
        
        wedges, texts, autotexts = ax1.pie(sizes, labels=categories, colors=colors, autopct='',
                                          startangle=90, explode=(0.05, 0.05, 0.05, 0.05, 0.05, 0.05))
        
        ax1.set_title('$500K Fund Allocation', fontsize=14, fontweight='bold')
        
        # Add amount labels
        for i, (wedge, amount) in enumerate(zip(wedges, amounts)):
            angle = (wedge.theta2 + wedge.theta1) / 2
            x = 0.7 * np.cos(np.radians(angle))
            y = 0.7 * np.sin(np.radians(angle))
            ax1.text(x, y, amount, ha='center', va='center', fontweight='bold', fontsize=12)
        
        # Chart 2: Timeline and Milestones
        months = ['Month 3', 'Month 6', 'Month 12', 'Month 18']
        users = [1_000, 10_000, 50_000, 100_000]
        revenue = [10_000, 100_000, 500_000, 1_000_000]  # Monthly revenue in USD
        
        ax2_twin = ax2.twinx()
        
        line1 = ax2.plot(months, users, marker='o', linewidth=3, color='#2ecc71', label='Users')
        line2 = ax2_twin.plot(months, revenue, marker='s', linewidth=3, color='#e74c3c', label='Monthly Revenue ($)')
        
        ax2.set_xlabel('Timeline', fontsize=12, fontweight='bold')
        ax2.set_ylabel('Active Users', fontsize=12, fontweight='bold', color='#2ecc71')
        ax2_twin.set_ylabel('Monthly Revenue ($)', fontsize=12, fontweight='bold', color='#e74c3c')
        ax2.set_title('Growth Milestones', fontsize=14, fontweight='bold')
        
        ax2.tick_params(axis='y', labelcolor='#2ecc71')
        ax2_twin.tick_params(axis='y', labelcolor='#e74c3c')
        
        # Format y-axis
        ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1e3:.0f}K'))
        ax2_twin.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e3:.0f}K' if x < 1e6 else f'${x/1e6:.1f}M'))
        
        # Add milestone annotations
        milestones = ['MVP Launch', 'Product-Market Fit', 'Break-Even', 'Series A Ready']
        for i, (month, milestone) in enumerate(zip(months, milestones)):
            ax2.annotate(milestone, xy=(i, users[i]), xytext=(i, users[i] + 15000),
                        ha='center', fontweight='bold', fontsize=10,
                        arrowprops=dict(arrowstyle='->', color='black'))
        
        plt.tight_layout()
        plt.savefig('funding_timeline.png', dpi=300, bbox_inches='tight')
        plt.show()

def main():
    """Generate all investor presentation charts"""
    print("📊 Generating NeuroSphere Investor Charts")
    print("=" * 50)
    
    charts = BusinessCaseCharts()
    
    print("📈 Creating market opportunity chart...")
    charts.create_market_opportunity_chart()
    
    print("🏆 Creating competitive advantage chart...")
    charts.create_competitive_advantage_chart()
    
    print("🪙 Creating tokenomics diagram...")
    charts.create_tokenomics_diagram()
    
    print("💰 Creating funding allocation chart...")
    charts.create_funding_allocation_chart()
    
    print("\n✅ All charts generated successfully!")
    print("📁 Files saved:")
    print("  • market_opportunity.png")
    print("  • competitive_analysis.png") 
    print("  • tokenomics_flow.png")
    print("  • funding_timeline.png")
    print("\n🎯 Ready for investor presentation!")

if __name__ == "__main__":
    main()
