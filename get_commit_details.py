import subprocess
import sys

def get_commit_details(commit_id):
    try:
        result=subprocess.run(['git', 'show', '--quiet',commit_id], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}",file=sys.stderr)
        return None
    
if __name__=="__main__":
    if len(sys.argv) !=2:
        print("Usage: python get_commit_details.py <commit_id)" , file=sys.stderr)
        sys.exit(1)

    commit_id=sys.argv[1]
    details=get_commit_details(commit_id)
    if details:
        print(details)       
