import requests
import json

def test_api():
    """Test the TDS Virtual TA API"""
    base_url = "http://localhost:8080"
    
    # Test questions
    test_questions = [
        "The question asks to use gpt-3.5-turbo-0125 model but the ai-proxy provided by Anand sir only supports gpt-4o-mini. So should we just use gpt-4o-mini or use the OpenAI API for gpt3.5 turbo?",
        "If a student scores 10/10 on GA4 as well as a bonus, how would it appear on the dashboard?",
        "I know Docker but have not used Podman before. Should I use Docker for this course?",
        "When is the TDS Sep 2025 end-term exam?"
    ]
    
    print("Testing TDS Virtual TA API...")
    print("=" * 50)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\nTest {i}: {question[:60]}...")
        
        try:
            response = requests.post(
                f"{base_url}/api/",
                headers={"Content-Type": "application/json"},
                json={"question": question},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Status: {response.status_code}")
                print(f"📝 Answer: {data['answer'][:100]}...")
                print(f"🔗 Links: {len(data['links'])} provided")
                
                # Validate response structure
                if 'answer' in data and 'links' in data:
                    if isinstance(data['links'], list):
                        print("✅ Response format is correct")
                    else:
                        print("❌ Links is not a list")
                else:
                    print("❌ Missing required fields")
            else:
                print(f"❌ Status: {response.status_code}")
                print(f"Error: {response.text}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {e}")
        
        print("-" * 50)

if __name__ == "__main__":
    test_api()
