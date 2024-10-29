from collections import Counter

def check_permutation_in_text(pattern, text):
    pattern_len = len(pattern)
    text_len = len(text)
    
    # Frequency map for the pattern
    pattern_count = Counter(pattern)
    
    # Frequency map for the first window in text
    window_count = Counter(text[:pattern_len])
    
    # Check initial window
    if window_count == pattern_count:
        return "YES"
    
    # Slide the window across the text
    for i in range(pattern_len, text_len):
        start_char = text[i - pattern_len]  # Char to remove from window
        new_char = text[i]  # Char to add to window
        
        # Remove one count of the start character
        if window_count[start_char] == 1:
            del window_count[start_char]
        else:
            window_count[start_char] -= 1
            
        # Add one count of the new character
        window_count[new_char] += 1
        
        # Check if window matches the pattern count
        if window_count == pattern_count:
            return "YES"
    
    return "NO"

# Input reading and handling multiple test cases
def main():
    T = int(input("Enter number of test cases: "))
    results = []
    for _ in range(T):
        pattern = input("Enter pattern: ").strip()
        text = input("Enter text: ").strip()
        results.append(check_permutation_in_text(pattern, text))
    print("\n".join(results))

# Uncomment below line to run the function if needed
main()
