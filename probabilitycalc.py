import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, number_of_balls):
        if number_of_balls >= len(self.contents):
            all_balls = self.contents.copy()
            self.contents = []
            return all_balls
        
        drawn_balls = []
        for _ in range(number_of_balls):
            if self.contents:
                ball = random.choice(self.contents)
                self.contents.remove(ball)
                drawn_balls.append(ball)
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # For counting balls by color
        drawn_balls_dict = {}
        for ball in drawn_balls:
            drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1
        
        # for checkong if we got at least the expected number of balls of each color
        success = True
        for color, count in expected_balls.items():
            if drawn_balls_dict.get(color, 0) < count:
                success = False
                break
        
        if success:
            success_count += 1
    
    return success_count / num_experiments

def test_hat_creation():
    hat = Hat(red=3, blue=2)
    actual_contents = hat.contents
    expected_contents_count = {'red': 0, 'blue': 0}
    
    for ball in actual_contents:
        expected_contents_count[ball] += 1
    
    assert expected_contents_count['red'] == 3, f"Expected 3 red balls, got {expected_contents_count['red']}"
    assert expected_contents_count['blue'] == 2, f"Expected 2 blue balls, got {expected_contents_count['blue']}"
    assert len(actual_contents) == 5, f"Expected 5 total balls, got {len(actual_contents)}"
    
    print("✓ Test 1 passed: Hat creation adds correct contents")

def test_draw_reduces_contents():
    hat = Hat(red=5, blue=2)
    initial_size = len(hat.contents)
    drawn_balls = hat.draw(2)
    
    assert len(drawn_balls) == 2, f"Expected to draw 2 balls, got {len(drawn_balls)}"
    assert len(hat.contents) == initial_size - 2, f"Expected {initial_size - 2} balls remaining, got {len(hat.contents)}"
    
    print("✓ Test 2 passed: Draw method reduces number of items in contents")

def test_draw_more_than_available():
    hat = Hat(red=5, blue=2)
    initial_contents = hat.contents.copy()
    drawn_balls = hat.draw(10)  # More than available
    
    assert len(drawn_balls) == 7, f"Expected to draw 7 balls, got {len(drawn_balls)}"
    assert len(hat.contents) == 0, f"Expected 0 balls remaining, got {len(hat.contents)}"
    
    # for check if all original balls were returned
    assert sorted(drawn_balls) == sorted(initial_contents), "Drawn balls don't match initial contents"
    
    print("✓ Test 3 passed: Draw method behaves correctly when number exceeds available balls")

def test_experiment_probability():
    hat1 = Hat(red=3, green=2)
    result1 = experiment(hat=hat1, expected_balls={"red": 1}, num_balls_drawn=1, num_experiments=1000)
    
    hat2 = Hat(red=3, green=2)
    result2 = experiment(hat=hat2, expected_balls={"red": 1, "green": 1}, num_balls_drawn=1, num_experiments=1000)
    
    assert 0 <= result1 <= 1, f"Probability must be between 0 and 1, got {result1}"
    assert 0 <= result2 <= 1, f"Probability must be between 0 and 1, got {result2}"
    assert result1 != result2, f"Different experiments should return different probabilities (got {result1} and {result2})"
    
    print("✓ Test 4 passed: Experiment method returns different probabilities for different scenarios")


if __name__ == "__main__":
    # Run the tests
    print("Running tests...")
    test_hat_creation()
    test_draw_reduces_contents()
    test_draw_more_than_available()
    test_experiment_probability()
    print("All tests passed!")
    
    print("\nRunning examples:")
    # Original example from the problem
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(
        hat=hat,
        expected_balls={"red": 2, "green": 1},
        num_balls_drawn=5,
        num_experiments=2000
    )
   
    
    