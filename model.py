"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
def expected_value(values, probabilities):
    np_val = np.array(values)
    np_probs = np.array(probabilities)
    return np.sum(np_val * np_probs)

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    narr = np.arange(1, sides + 1, dtype=float)
    probs = np.ones(sides) / sides
    mu = expected_value(narr, probs)
    reroll_mask = narr < mu
    rerolled_values = narr[reroll_mask].astype(int).tolist()
    narr[reroll_mask] = mu

    return {
        "value": np.mean(narr), 
        "reroll_faces": rerolled_values
    }

# Step 3 - pay_per_reroll_die_game (not yet solved)
# TODO: implement

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

