"""Visualize cryptocurrency market data from the database."""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import config


def load_data_from_db():
    """Load cryptocurrency data from SQLite database."""
    conn = sqlite3.connect(config.DB_PATH)
    query = f"SELECT * FROM {config.CRYPTO_TABLE}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


def create_bar_chart(df, top_n=10):
    """Create bar chart of top cryptocurrencies by market cap."""
    top_cryptos = df.head(top_n)

    plt.figure(figsize=(12, 6))
    plt.bar(top_cryptos['Name'], top_cryptos['MarketCap'], color='steelblue')
    plt.xlabel('Cryptocurrency', fontsize=12)
    plt.ylabel('Market Cap (USD)', fontsize=12)
    plt.title(f'Top {top_n} Cryptocurrencies by Market Cap', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.ticklabel_format(style='plain', axis='y')
    plt.tight_layout()
    plt.savefig('charts/market_cap_bar.png', dpi=300, bbox_inches='tight')
    print("✓ Bar chart saved: charts/market_cap_bar.png")


def create_pie_chart(df, top_n=10):
    """Create pie chart of market share distribution."""
    top_cryptos = df.head(top_n)

    plt.figure(figsize=(10, 8))
    plt.pie(top_cryptos['MarketCap'], labels=top_cryptos['Name'], autopct='%1.1f%%', startangle=90)
    plt.title(f'Market Share - Top {top_n} Cryptocurrencies', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('charts/market_share_pie.png', dpi=300, bbox_inches='tight')
    print("✓ Pie chart saved: charts/market_share_pie.png")


def create_price_chart(df, top_n=15):
    """Create horizontal bar chart of cryptocurrency prices."""
    top_cryptos = df.head(top_n)

    plt.figure(figsize=(10, 8))
    plt.barh(top_cryptos['Name'], top_cryptos['PriceUSD'], color='coral')
    plt.xlabel('Price (USD)', fontsize=12)
    plt.ylabel('Cryptocurrency', fontsize=12)
    plt.title(f'Top {top_n} Cryptocurrency Prices', fontsize=14, fontweight='bold')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('charts/price_comparison.png', dpi=300, bbox_inches='tight')
    print("✓ Price chart saved: charts/price_comparison.png")


def create_scatter_plot(df):
    """Create scatter plot of Price vs Market Cap."""
    plt.figure(figsize=(12, 6))
    plt.scatter(df['PriceUSD'], df['MarketCap'], alpha=0.6, c='green', edgecolors='black')

    # Annotate top 5
    top5 = df.head(5)
    for _, row in top5.iterrows():
        plt.annotate(row['Symbol'].upper(),
                    (row['PriceUSD'], row['MarketCap']),
                    xytext=(5, 5), textcoords='offset points', fontsize=9)

    plt.xlabel('Price (USD)', fontsize=12)
    plt.ylabel('Market Cap (USD)', fontsize=12)
    plt.title('Cryptocurrency Price vs Market Cap', fontsize=14, fontweight='bold')
    plt.ticklabel_format(style='plain', axis='y')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig('charts/price_vs_marketcap.png', dpi=300, bbox_inches='tight')
    print("✓ Scatter plot saved: charts/price_vs_marketcap.png")


def generate_summary(df):
    """Print summary statistics."""
    print("\n" + "="*50)
    print("CRYPTOCURRENCY MARKET SUMMARY")
    print("="*50)
    print(f"Total cryptocurrencies: {len(df)}")
    print(f"Top cryptocurrency: {df.iloc[0]['Name']} (${df.iloc[0]['MarketCap']:,.0f})")
    print(f"Highest price: {df.loc[df['PriceUSD'].idxmax(), 'Name']} (${df['PriceUSD'].max():,.2f})")
    print(f"Average market cap: ${df['MarketCap'].mean():,.0f}")
    print("="*50 + "\n")


def main():
    """Main function to generate all visualizations."""
    import os

    # Create charts directory if it doesn't exist
    os.makedirs('charts', exist_ok=True)

    print("Loading data from database...")
    df = load_data_from_db()
    print(f"✓ Loaded {len(df)} cryptocurrencies\n")

    # Generate summary
    generate_summary(df)

    # Create visualizations
    print("Generating charts...")
    create_bar_chart(df, top_n=10)
    create_pie_chart(df, top_n=10)
    create_price_chart(df, top_n=15)
    create_scatter_plot(df)

    print("\n✓ All visualizations complete!")
    print("Charts saved in the 'charts/' folder")


if __name__ == "__main__":
    main()
