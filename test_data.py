import json
import os

def test_projects_data_integrity():
    json_path = r'C:\Users\SHAURYA MISHRA\.gemini\antigravity\scratch\antigravity-roadmap\projects.json'
    assert os.path.exists(json_path), "projects.json file does not exist!"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    assert isinstance(data, dict), "Root element should be a dictionary/object"
    assert len(data) == 10, f"Expected 10 categories, found {len(data)}"
    
    total_projects = 0
    categories = [
        "Web Development", "AI & Machine Learning", "Data & Analytics", 
        "Developer Tools & CLI", "Games & Interactive", "Cloud & DevOps", 
        "Mobile & PWA", "IoT & Hardware", "Security & Auth", "Creative & Media"
    ]
    
    for cat in categories:
        assert cat in data, f"Category '{cat}' missing from projects database!"
        projects_list = data[cat]
        assert isinstance(projects_list, list), f"Projects in '{cat}' should be a list"
        
        for idx, proj in enumerate(projects_list):
            # Skip empty placeholders
            if not proj:
                continue
            
            total_projects += 1
            # Check fields
            assert "name" in proj, f"Project {idx} in {cat} missing 'name'"
            assert "desc" in proj, f"Project {idx} in {cat} missing 'desc'"
            assert "tech" in proj, f"Project {idx} in {cat} missing 'tech'"
            assert "difficulty" in proj, f"Project {idx} in {cat} missing 'difficulty'"
            assert "time" in proj, f"Project {idx} in {cat} missing 'time'"
            
            # Check types
            assert isinstance(proj["name"], str), f"Project {idx} name should be string"
            assert isinstance(proj["desc"], str), f"Project {idx} desc should be string"
            assert isinstance(proj["tech"], list), f"Project {idx} tech should be a list"
            assert isinstance(proj["difficulty"], str), f"Project {idx} difficulty should be a string"
            assert isinstance(proj["time"], str), f"Project {idx} time should be a string"
            
            # Check difficulty levels
            assert proj["difficulty"] in ["Beginner", "Intermediate", "Advanced", "Expert"], \
                f"Invalid difficulty '{proj['difficulty']}' in project '{proj['name']}'"
                
    print(f"PASS: Data integrity validated for {total_projects} projects across 10 categories!")

if __name__ == "__main__":
    try:
        test_projects_data_integrity()
        print("ALL TESTS PASSED SUCCESSFULLY!")
    except AssertionError as e:
        print("TEST FAILED:", e)
        exit(1)
