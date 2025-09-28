# ============================================================================
# MAIN EXECUTION SCRIPT
# ============================================================================

def main():
    """Main execution function"""
    print("🎯 Automated Data Pipeline - Retail Orders Analytics")
    print("📊 Implementing Bronze-Silver-Gold Architecture")
    print("="*60)
    
    # Initialize configuration
    config = PipelineConfig()
    
    # Initialize and run pipeline
    pipeline = DataPipeline(config)
    result = pipeline.run_pipeline()
    
    # Print results
    if result['status'] == 'success':
        print("\n🎉 PIPELINE EXECUTION SUCCESSFUL!")
        print(f"📊 Bronze Records: {result['bronze_records']:,}")
        print(f"🔧 Silver Records: {result['silver_records']:,}")
        print(f"💎 Gold Records: {sum(result['gold_records'].values()):,}")
        print("\n📄 Generated Files:")
        print("   - retail_dwh.db (SQLite database)")
        print("   - pipeline_execution.log (Execution log)")
        print("   - pipeline_execution_report.csv (Summary report)")
    else:
        print(f"\n❌ PIPELINE FAILED: {result['error']}")
    
    print("="*60)
