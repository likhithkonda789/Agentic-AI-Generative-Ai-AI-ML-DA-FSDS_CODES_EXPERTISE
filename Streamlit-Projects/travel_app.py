import streamlit as st
import pandas as pd
import datetime as dt

# =========================
#  CONFIG & GLOBAL SETTINGS
# =========================

st.set_page_config(
    page_title="Goa Travel Planner",
    page_icon="✈️",
    layout="wide",
)

# Custom CSS for modern blue/white theme and card-style layout
st.markdown(
    """
    <style>
    /* Global font and background */
    body, .stApp {
        background-color: #f5f7fb;
        font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main title */
    .main-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: #0b5ed7;
        margin-bottom: 0.1rem;
    }

    .sub-title {
        font-size: 0.98rem;
        color: #6c757d;
        margin-bottom: 1.2rem;
    }

    /* Card container */
    .card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.8rem;
        border: 1px solid #e2e6f0;
        box-shadow: 0 4px 8px rgba(15, 23, 42, 0.04);
    }

    .card-header {
        font-weight: 600;
        font-size: 1.02rem;
        color: #0b5ed7;
        margin-bottom: 0.2rem;
    }

    .pill {
        display: inline-block;
        padding: 0.18rem 0.6rem;
        border-radius: 999px;
        background-color: #e7f1ff;
        color: #0b5ed7;
        font-size: 0.75rem;
        margin-right: 0.35rem;
        margin-top: 0.15rem;
    }

    .price-text {
        font-size: 1.05rem;
        font-weight: 700;
        color: #198754;
    }

    .rating {
        color: #ffc107;
        font-weight: 600;
        font-size: 0.9rem;
    }

    .section-label {
        font-size: 0.78rem;
        font-weight: 600;
        color: #6c757d;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }

    /* Make buttons a bit more rounded */
    .stButton>button {
        border-radius: 999px;
        border: 1px solid #0b5ed7;
        padding: 0.4rem 1.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
#  DUMMY DATASETS
# =========================

def load_flight_data() -> pd.DataFrame:
    """Simulate flight data for HYD -> GOA round trip."""
    data = [
        {
            "airline": "IndiGo",
            "departure_time": "06:30",
            "arrival_time": "08:00",
            "duration": "1h 30m",
            "price": 4500,
            "dep_period": "Morning",
        },
        {
            "airline": "Air India",
            "departure_time": "09:45",
            "arrival_time": "11:30",
            "duration": "1h 45m",
            "price": 5200,
            "dep_period": "Morning",
        },
        {
            "airline": "Vistara",
            "departure_time": "13:10",
            "arrival_time": "15:00",
            "duration": "1h 50m",
            "price": 5800,
            "dep_period": "Afternoon",
        },
        {
            "airline": "SpiceJet",
            "departure_time": "18:20",
            "arrival_time": "20:05",
            "duration": "1h 45m",
            "price": 4100,
            "dep_period": "Evening",
        },
        {
            "airline": "IndiGo",
            "departure_time": "21:15",
            "arrival_time": "23:00",
            "duration": "1h 45m",
            "price": 3900,
            "dep_period": "Night",
        },
    ]
    df = pd.DataFrame(data)
    df = df.sort_values("price", ascending=True)
    return df


def load_stay_data() -> pd.DataFrame:
    """Simulate stays (hotels & homestays) in Goa."""
    data = [
        {
            "name": "Sea Breeze Homestay",
            "type": "Homestay",
            "price_per_night": 2200,
            "rating": 4.5,
            "amenities": "WiFi, Breakfast, AC, Near Beach",
        },
        {
            "name": "Goa Azure Resort",
            "type": "Hotel",
            "price_per_night": 3800,
            "rating": 4.7,
            "amenities": "Pool, WiFi, Bar, AC, Restaurant",
        },
        {
            "name": "Palm Grove Villa",
            "type": "Homestay",
            "price_per_night": 2600,
            "rating": 4.3,
            "amenities": "Kitchen, WiFi, AC, Parking",
        },
        {
            "name": "Lagoon View Hotel",
            "type": "Hotel",
            "price_per_night": 3200,
            "rating": 4.2,
            "amenities": "Pool, WiFi, Breakfast, AC",
        },
        {
            "name": "Beachfront Paradise",
            "type": "Hotel",
            "price_per_night": 5400,
            "rating": 4.9,
            "amenities": "Private Beach, Pool, Bar, Spa, WiFi",
        },
    ]
    df = pd.DataFrame(data)
    df = df.sort_values("price_per_night", ascending=True)
    return df


def load_restaurant_data() -> pd.DataFrame:
    """Simulate restaurant recommendations in Goa."""
    data = [
        {
            "name": "Coastal Spice Shack",
            "cuisine": "Goan, Seafood",
            "rating": 4.6,
            "approx_cost_for_two": 900,
            "segment": "Budget",
        },
        {
            "name": "Bayfront Bistro",
            "cuisine": "Continental, Seafood",
            "rating": 4.4,
            "approx_cost_for_two": 1500,
            "segment": "Mid-range",
        },
        {
            "name": "Casa Portuguesa",
            "cuisine": "Portuguese, Goan",
            "rating": 4.8,
            "approx_cost_for_two": 2000,
            "segment": "Premium",
        },
        {
            "name": "Shoreline Cafe",
            "cuisine": "Cafe, Fast Food",
            "rating": 4.2,
            "approx_cost_for_two": 700,
            "segment": "Budget",
        },
        {
            "name": "Skyline Rooftop",
            "cuisine": "Indian, Fusion",
            "rating": 4.5,
            "approx_cost_for_two": 1800,
            "segment": "Mid-range",
        },
    ]
    df = pd.DataFrame(data)
    df = df.sort_values("approx_cost_for_two", ascending=True)
    return df


# =========================
#  SESSION STATE HELPERS
# =========================

if "selected_flight" not in st.session_state:
    st.session_state.selected_flight = None

if "selected_stay" not in st.session_state:
    st.session_state.selected_stay = None

if "selected_restaurant" not in st.session_state:
    st.session_state.selected_restaurant = None


# =========================
#  TRIP CONFIG / SIDEBAR
# =========================

with st.sidebar:
    st.markdown("### ✈️ Trip Details")
    st.write("Fixed route: **Hyderabad (HYD) → Goa (GOA)**")
    st.caption("Round Trip · 2 Days, 2 Nights")

    # Date pickers
    today = dt.date.today()
    default_depart = today + dt.timedelta(days=7)
    default_return = default_depart + dt.timedelta(days=2)

    depart_date = st.date_input("Departure Date", value=default_depart)
    return_date = st.date_input("Return Date", value=default_return)

    # Number of travelers
    travelers = st.number_input(
        "Number of Travelers",
        min_value=1,
        max_value=10,
        value=1,
        step=1,
    )

    st.markdown("---")
    st.markdown("##### ℹ️ Trip Info")
    st.markdown(
        f"""
        - **Source**: Hyderabad (HYD)  
        - **Destination**: Goa (GOA)  
        - **Trip Type**: Round Trip  
        - **Duration**: 2 Days, 2 Nights  
        - **Travelers**: {travelers}
        """
    )


# =========================
#  PAGE HEADER
# =========================

st.markdown('<div class="main-title">Goa Travel Planner</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Plan your flights, stays, and restaurants in Goa with a clean, MakeMyTrip-style interface.</div>',
    unsafe_allow_html=True,
)


# =========================
#  LOAD DATA
# =========================

flights_df = load_flight_data()
stays_df = load_stay_data()
restaurants_df = load_restaurant_data()


# =========================
#  TABS LAYOUT
# =========================

tab_flights, tab_stays, tab_restaurants, tab_summary = st.tabs(
    ["✈️ Flights", "🏨 Stays", "🍽️ Restaurants", "📋 Summary"]
)


# =========================
#  FLIGHTS TAB
# =========================

with tab_flights:
    st.markdown("#### ✈️ Choose Your Flight")

    # Filters row
    col_price, col_dep, col_airline = st.columns([2, 2, 2])

    with col_price:
        st.markdown('<span class="section-label">Price Range (per person)</span>', unsafe_allow_html=True)
        min_price, max_price = int(flights_df["price"].min()), int(flights_df["price"].max())
        price_range = st.slider(
            "Price Range",
            min_value=min_price,
            max_value=max_price,
            value=(min_price, max_price),
            step=100,
            label_visibility="collapsed",
        )

    with col_dep:
        st.markdown('<span class="section-label">Departure Time</span>', unsafe_allow_html=True)
        dep_periods = ["Morning", "Afternoon", "Evening", "Night"]
        dep_filter = st.multiselect(
            "Departure Time",
            dep_periods,
            default=dep_periods,
            label_visibility="collapsed",
        )

    with col_airline:
        st.markdown('<span class="section-label">Airlines</span>', unsafe_allow_html=True)
        airlines = sorted(flights_df["airline"].unique().tolist())
        airline_filter = st.multiselect(
            "Airlines",
            airlines,
            default=airlines,
            label_visibility="collapsed",
        )

    # Apply filters
    f_flights = flights_df[
        (flights_df["price"].between(price_range[0], price_range[1]))
        & (flights_df["dep_period"].isin(dep_filter))
        & (flights_df["airline"].isin(airline_filter))
    ].copy()

    st.caption(f"Showing {len(f_flights)} flight option(s), sorted by lowest price.")

    # Render cards
    for idx, row in f_flights.iterrows():
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)

            c1, c2, c3, c4 = st.columns([3, 3, 2, 2])

            with c1:
                st.markdown(
                    f'<div class="card-header">🛫 {row["airline"]}</div>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<span class="pill">HYD → GOA</span> '
                    f'<span class="pill">{row["dep_period"]}</span>',
                    unsafe_allow_html=True,
                )

            with c2:
                st.markdown('<span class="section-label">Timing</span>', unsafe_allow_html=True)
                st.write(f"**{row['departure_time']} → {row['arrival_time']}**")
                st.caption(f"Duration: {row['duration']}")

            with c3:
                st.markdown('<span class="section-label">Price</span>', unsafe_allow_html=True)
                st.markdown(
                    f'<span class="price-text">₹ {int(row["price"]):,}</span> / person',
                    unsafe_allow_html=True,
                )

            with c4:
                st.markdown('<span class="section-label">Action</span>', unsafe_allow_html=True)
                if st.button(
                    "Select Flight",
                    key=f"select_flight_{idx}",
                    use_container_width=True,
                ):
                    st.session_state.selected_flight = row.to_dict()
                    st.success("Flight selected for your trip!")

            st.markdown("</div>", unsafe_allow_html=True)


# =========================
#  STAYS TAB
# =========================

with tab_stays:
    st.markdown("#### 🏨 Select Your Stay in Goa")

    col_price, col_type = st.columns([2, 2])

    with col_price:
        st.markdown('<span class="section-label">Price / Night</span>', unsafe_allow_html=True)
        min_pn, max_pn = int(stays_df["price_per_night"].min()), int(stays_df["price_per_night"].max())
        stay_price_range = st.slider(
            "Price / Night",
            min_value=min_pn,
            max_value=max_pn,
            value=(min_pn, max_pn),
            step=100,
            label_visibility="collapsed",
        )

    with col_type:
        st.markdown('<span class="section-label">Property Type</span>', unsafe_allow_html=True)
        stay_types = sorted(stays_df["type"].unique().tolist())
        stay_type_filter = st.multiselect(
            "Property Type",
            stay_types,
            default=stay_types,
            label_visibility="collapsed",
        )

    # Apply filters
    f_stays = stays_df[
        (stays_df["price_per_night"].between(stay_price_range[0], stay_price_range[1]))
        & (stays_df["type"].isin(stay_type_filter))
    ].copy()

    st.caption(f"Showing {len(f_stays)} stay option(s), sorted by lowest price.")

    for idx, row in f_stays.iterrows():
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)

            c1, c2, c3 = st.columns([4, 3, 2])

            with c1:
                st.markdown(
                    f'<div class="card-header">🏨 {row["name"]}</div>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<span class="pill">{row["type"]}</span>',
                    unsafe_allow_html=True,
                )
                st.caption(row["amenities"])

            with c2:
                st.markdown('<span class="section-label">Price & Rating</span>', unsafe_allow_html=True)
                st.markdown(
                    f'<span class="price-text">₹ {int(row["price_per_night"]):,}</span> / night',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<span class="rating">⭐ {row["rating"]:.1f}</span>',
                    unsafe_allow_html=True,
                )

            with c3:
                st.markdown('<span class="section-label">Action</span>', unsafe_allow_html=True)
                if st.button(
                    "Select Stay",
                    key=f"select_stay_{idx}",
                    use_container_width=True,
                ):
                    st.session_state.selected_stay = row.to_dict()
                    st.success("Stay selected for your trip!")

            st.markdown("</div>", unsafe_allow_html=True)


# =========================
#  RESTAURANTS TAB
# =========================

with tab_restaurants:
    st.markdown("#### 🍽️ Top Restaurants in Goa")

    col_cost, col_seg = st.columns([2, 2])

    with col_cost:
        st.markdown('<span class="section-label">Approx Cost for Two</span>', unsafe_allow_html=True)
        min_cost, max_cost = (
            int(restaurants_df["approx_cost_for_two"].min()),
            int(restaurants_df["approx_cost_for_two"].max()),
        )
        cost_range = st.slider(
            "Approx cost for two",
            min_value=min_cost,
            max_value=max_cost,
            value=(min_cost, max_cost),
            step=100,
            label_visibility="collapsed",
        )

    with col_seg:
        st.markdown('<span class="section-label">Segment</span>', unsafe_allow_html=True)
        segments = sorted(restaurants_df["segment"].unique().tolist())
        seg_filter = st.multiselect(
            "Segment",
            segments,
            default=segments,
            label_visibility="collapsed",
        )

    # Apply filters
    f_rest = restaurants_df[
        (restaurants_df["approx_cost_for_two"].between(cost_range[0], cost_range[1]))
        & (restaurants_df["segment"].isin(seg_filter))
    ].copy()

    st.caption(f"Showing {len(f_rest)} restaurant option(s), sorted from budget to premium.")

    for idx, row in f_rest.iterrows():
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)

            c1, c2, c3 = st.columns([4, 3, 2])

            with c1:
                st.markdown(
                    f'<div class="card-header">🍽️ {row["name"]}</div>',
                    unsafe_allow_html=True,
                )
                st.caption(row["cuisine"])

            with c2:
                st.markdown('<span class="section-label">Rating & Cost</span>', unsafe_allow_html=True)
                st.markdown(
                    f'<span class="rating">⭐ {row["rating"]:.1f}</span>',
                    unsafe_allow_html=True,
                )
                st.markdown(
                    f'<span class="price-text">₹ {int(row["approx_cost_for_two"]):,}</span> for two',
                    unsafe_allow_html=True,
                )
                st.caption(f"Segment: {row['segment']}")

            with c3:
                st.markdown('<span class="section-label">Action</span>', unsafe_allow_html=True)
                if st.button(
                    "Select Restaurant",
                    key=f"select_restaurant_{idx}",
                    use_container_width=True,
                ):
                    st.session_state.selected_restaurant = row.to_dict()
                    st.success("Restaurant preference saved!")

            st.markdown("</div>", unsafe_allow_html=True)


# =========================
#  SUMMARY & COST TAB
# =========================

with tab_summary:
    st.markdown("#### 📋 Trip Summary & Total Cost")

    selected_flight = st.session_state.selected_flight
    selected_stay = st.session_state.selected_stay
    selected_restaurant = st.session_state.selected_restaurant

    nights = 2  # Fixed: 2 nights
    days = 2    # Fixed: 2 days

    # Compute costs
    flight_cost_total = (
        selected_flight["price"] * travelers if selected_flight is not None else 0
    )
    stay_cost_total = (
        selected_stay["price_per_night"] * nights * travelers if selected_stay is not None else 0
    )
    # Assume restaurant cost for two per day; scale by travelers
    restaurant_cost_total = 0
    if selected_restaurant is not None:
        per_two_per_day = selected_restaurant["approx_cost_for_two"]
        # cost per person per day
        per_person_per_day = per_two_per_day / 2
        restaurant_cost_total = per_person_per_day * days * travelers

    grand_total = flight_cost_total + stay_cost_total + restaurant_cost_total

    col_summary, col_cost = st.columns([3, 2])

    with col_summary:
        st.markdown('<span class="section-label">Selections</span>', unsafe_allow_html=True)

        if selected_flight:
            st.markdown("##### ✈️ Flight")
            st.write(
                f"**{selected_flight['airline']}** · "
                f"{selected_flight['departure_time']} → {selected_flight['arrival_time']} · "
                f"{selected_flight['duration']}"
            )
            st.caption(f"Price: ₹ {int(selected_flight['price']):,} per person")

        else:
            st.info("No flight selected yet. Go to the **Flights** tab to choose one.")

        if selected_stay:
            st.markdown("##### 🏨 Stay")
            st.write(
                f"**{selected_stay['name']}** · {selected_stay['type']} · "
                f"⭐ {selected_stay['rating']:.1f}"
            )
            st.caption(
                f"₹ {int(selected_stay['price_per_night']):,} per night · "
                f"{nights} nights · Amenities: {selected_stay['amenities']}"
            )
        else:
            st.info("No stay selected yet. Go to the **Stays** tab to choose one.")

        if selected_restaurant:
            st.markdown("##### 🍽️ Restaurant")
            st.write(f"**{selected_restaurant['name']}** · {selected_restaurant['cuisine']}")
            st.caption(
                f"Approx ₹ {int(selected_restaurant['approx_cost_for_two']):,} for two · "
                f"Segment: {selected_restaurant['segment']}"
            )
        else:
            st.info(
                "No restaurant preference selected yet. Go to the **Restaurants** tab to pick one."
            )

    with col_cost:
        st.markdown('<span class="section-label">Total Trip Cost</span>', unsafe_allow_html=True)
        st.markdown(
            f"""
            #### 💰 Estimated Cost (for {travelers} traveler(s))
            - Flights: **₹ {int(flight_cost_total):,}**
            - Stay ({nights} nights): **₹ {int(stay_cost_total):,}**
            - Food ({days} days): **₹ {int(restaurant_cost_total):,}**
            
            **Grand Total: ₹ {int(grand_total):,}**
            """,
            unsafe_allow_html=False,
        )

        # Booking button (dummy)
        can_book = selected_flight and selected_stay
        if st.button(
            "Book This Trip",
            use_container_width=True,
            disabled=not can_book,
        ):
            st.success("🎉 Booking initiated! (Demo only – no real payment processed.)")

        if not can_book:
            st.caption("Select at least a flight and a stay to enable booking.")

    st.markdown("---")
    st.caption(
        "Note: All prices and details are simulated for demo purposes only. "
        "Use live APIs for real-world deployments."
    )

