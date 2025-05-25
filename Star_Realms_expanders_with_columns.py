
import streamlit as st
from collections import Counter

# Define the Player class
class Player:
    def __init__(self, name, loyalty=50, coin=0, damage=0):
        self.name = name
        self.loyalty = loyalty
        self.coin = coin
        self.damage = damage

# Set the page configuration
st.set_page_config(layout="wide")

# Title of the app
st.title("Star Realms Counter by cernyxd")

# Initialize session state variables
if "play_clicked" not in st.session_state:
    st.session_state.play_clicked = False
if "num_players" not in st.session_state:
    st.session_state.num_players = None
if "button_states" not in st.session_state:
    st.session_state.button_states = {}

# Layout for player name input
col1, col2 = st.columns([2, 3])

if not st.session_state.play_clicked:
    player_names = []
    for i in range(4):
        player_name = st.text_input(f"Player {i+1} name:", key=f"player_name_{i+1}", max_chars=9)
        if player_name:
            player_names.append(player_name)

    # Update number of players based on non-empty names
    st.session_state.num_players = len(player_names)

    duplicate_names_exist = False
    if len(player_names) > 1:
        name_counts = Counter(player_names)
        duplicates = [name for name, count in name_counts.items() if count > 1]

        if duplicates:
            st.warning(f"Duplicate names found: {', '.join(duplicates)}")
            duplicate_names_exist = True
        else:
            st.success("All player names are unique")

    with col2:
        play_button = st.button("Play!", disabled=duplicate_names_exist or len(player_names) == 0)

    if play_button and not duplicate_names_exist:
        st.session_state.play_clicked = True
        st.rerun()

    st.session_state.player_names = player_names

if st.session_state.play_clicked:
    if "players" not in st.session_state:
        st.session_state.players = [Player(name) for name in st.session_state.player_names]

    for player in st.session_state.players:
        if player.name not in st.session_state.button_states:
            st.session_state.button_states[player.name] = {
                "loyalty": False, "coin": False, "damage": False,
                "loyalty_minus": False, "coin_minus": False, "damage_minus": False
            }

        with st.expander(f"{player.name}"):
            st.markdown(f"<p style='text-align: center; font-size: 30px; font-weight: bold;'>{player.name}</p>", unsafe_allow_html=True)

            col1, col2, col3 = st.columns(3)

            def toggle_category(category, player_name):
                st.session_state.button_states[player_name][category] = not st.session_state.button_states[player_name][category]
                st.rerun()

            # Loyalty buttons
            with col1:
                if not st.session_state.button_states[player.name]["loyalty"]:
                    if st.button("Loyalty+", key=f"{player.name}_toggle_loyalty"):
                        toggle_category("loyalty", player.name)
                else:
                    c1, c2, c3 = st.columns(3)  # Create columns for inline buttons
                    with c1:
                        if st.button("1", key=f"{player.name}_loyalty_1"):
                            player.loyalty += 1
                            toggle_category("loyalty", player.name)
                    with c2:
                        if st.button("3", key=f"{player.name}_loyalty_3"):
                            player.loyalty += 3
                            toggle_category("loyalty", player.name)
                    with c3:
                        if st.button("5", key=f"{player.name}_loyalty_5"):
                            player.loyalty += 5
                            toggle_category("loyalty", player.name)

                st.write(f"**{player.loyalty} Loyalty**")

            # Coin buttons
            with col2:
                if not st.session_state.button_states[player.name]["coin"]:
                    if st.button("Coin+", key=f"{player.name}_toggle_coin"):
                        toggle_category("coin", player.name)
                else:
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        if st.button("1", key=f"{player.name}_coin_1"):
                            player.coin += 1
                            toggle_category("coin", player.name)
                    with c2:
                        if st.button("3", key=f"{player.name}_coin_3"):
                            player.coin += 3
                            toggle_category("coin", player.name)
                    with c3:
                        if st.button("5", key=f"{player.name}_coin_5"):
                            player.coin += 5
                            toggle_category("coin", player.name)

                st.write(f"**{player.coin} Coins**")

            # Damage buttons
            with col3:
                if not st.session_state.button_states[player.name]["damage"]:
                    if st.button("Damage+", key=f"{player.name}_toggle_damage"):
                        toggle_category("damage", player.name)
                else:
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        if st.button("1", key=f"{player.name}_damage_1"):
                            player.damage += 1
                            toggle_category("damage", player.name)
                    with c2:
                        if st.button("3", key=f"{player.name}_damage_3"):
                            player.damage += 3
                            toggle_category("damage", player.name)
                    with c3:
                        if st.button("5", key=f"{player.name}_damage_5"):
                            player.damage += 5
                            toggle_category("damage", player.name)

                st.write(f"**{player.damage} Damage**")

            # Loyalty minus buttons
            with col1:
                if not st.session_state.button_states[player.name]["loyalty_minus"]:
                    if st.button("Loyalty-", key=f"{player.name}_toggle_loyalty_minus"):
                        toggle_category("loyalty_minus", player.name)
                else:
                    c1, c2, c3 = st.columns(3)  # Create columns for inline buttons
                    with c1:
                        if st.button("1", key=f"{player.name}_loyalty_minus_1"):
                            player.loyalty -= 1
                            toggle_category("loyalty_minus", player.name)
                    with c2:
                        if st.button("3", key=f"{player.name}_loyalty_minus_3"):
                            player.loyalty -= 3
                            toggle_category("loyalty_minus", player.name)
                    with c3:
                        if st.button("5", key=f"{player.name}_loyalty_minus_5"):
                            player.loyalty -= 5
                            toggle_category("loyalty_minus", player.name)

            # Coin minus buttons
            with col2:
                if not st.session_state.button_states[player.name]["coin_minus"]:
                    if st.button("Coin -", key=f"{player.name}_toggle_coin_minus"):
                        toggle_category("coin_minus", player.name)
                else:
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        if st.button("1", key=f"{player.name}_coin_minus_1"):
                            player.coin -= 1
                            toggle_category("coin_minus", player.name)
                    with c2:
                        if st.button("3", key=f"{player.name}_coin_minus_3"):
                            player.coin -= 3
                            toggle_category("coin_minus", player.name)
                    with c3:
                        if st.button("5", key=f"{player.name}_coin_minus_5"):
                            player.coin -= 5
                            toggle_category("coin_minus", player.name)

            # Damage minus buttons
            with col3:
                if not st.session_state.button_states[player.name]["damage_minus"]:
                    if st.button("Damage -", key=f"{player.name}_toggle_damage_minus"):
                        toggle_category("damage_minus", player.name)
                else:
                    c1, c2, c3 = st.columns(3)
                    with c1:
                        if st.button("1", key=f"{player.name}_damage_minus_1"):
                            player.damage -= 1
                            toggle_category("damage_minus", player.name)
                    with c2:
                        if st.button("3", key=f"{player.name}_damage_minus_3"):
                            player.damage -= 3
                            toggle_category("damage_minus", player.name)
                    with c3:
                        if st.button("5", key=f"{player.name}_damage_minus_5"):
                            player.damage -= 5
                            toggle_category("damage_minus", player.name)

            st.markdown("<hr>", unsafe_allow_html=True)
