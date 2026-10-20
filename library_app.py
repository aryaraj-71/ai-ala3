import streamlit as st

# -----------------------------------------------------------------------------
# Page Configuration & UI Branding
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Central Library Desk Bot",
    page_icon="📚",
    layout="centered"
)

st.title("📚 Central Library Helpdesk")
st.caption("Rule-Based Library Assistant | GMIU Knowledge Resource Centre")

# -----------------------------------------------------------------------------
# Core Rule-Based Decision Logic (if-elif-else)
# -----------------------------------------------------------------------------
def get_library_response(user_input: str) -> str:
    text = user_input.lower().strip()

    # Rule 1: Greetings
    if text in ["hi", "hello", "hey", "good morning", "good evening", "namaste"]:
        return (
            "Hello! Welcome to the Central Library Helpdesk. "
            "How can I assist you with book searches, borrowing rules, fines, or digital resources today?"
        )

    # Rule 2: Bot Identity & Capabilities
    elif "who are you" in text or "what can you do" in text or "your name" in text:
        return (
            "I am the Central Library Assistant Bot. You can ask me about:\n"
            "• Library timings and open days\n"
            "• Book borrowing and return limits\n"
            "• Late return fines and renewal rules\n"
            "• Available catalog sections (Engineering, AI, Management)\n"
            "• E-journals, IEEE access, and study room facilities"
        )

    # Rule 3: Operating Hours & Working Days
    elif "time" in text or "timing" in text or "hour" in text or "open" in text or "sunday" in text:
        return (
            "**Library Operating Hours:**\n"
            "• Monday to Saturday: 8:00 AM - 8:00 PM\n"
            "• Reading Hall: 7:30 AM - 10:00 PM (Daily)\n"
            "• Sundays & Public Holidays: Closed (except during semester exam weeks)"
        )

    # Rule 4: Borrowing Limits & Eligibility
    elif "borrow" in text or "issue" in text or "how many books" in text or "limit" in text:
        return (
            "**Borrowing Guidelines:**\n"
            "• **Diploma / UG Students:** Up to 3 books for 14 calendar days\n"
            "• **PG Students:** Up to 5 books for 21 calendar days\n"
            "• **Faculty Members:** Up to 8 books for 90 days\n"
            "A valid Student ID Card is mandatory at the circulation counter."
        )

    # Rule 5: Book Renewal / Extension
    elif "renew" in text or "extend" in text or "extension" in text:
        return (
            "Books can be renewed up to **2 consecutive times** provided no other student "
            "has placed a reservation hold. Renewals can be done via the Online Library OPAC portal "
            "or at the circulation desk before the due date."
        )

    # Rule 6: Overdue Fine & Penalties
    elif "fine" in text or "penalty" in text or "late" in text or "charges" in text:
        return (
            "**Overdue Fine Policy:**\n"
            "• Standard collection: ₹2 per book per day for the first 7 days, and ₹5 per day thereafter.\n"
            "• Reference section books cannot be borrowed overnight (fine: ₹20 per day).\n"
            "All pending dues must be cleared prior to mid-term and semester hall ticket distribution."
        )

    # Rule 7: Book Search & Department Sections
    elif "book" in text or "find" in text or "search" in text or "subject" in text or "category" in text:
        return (
            "**Library Sections Available:**\n"
            "1. Computer Engineering & IT (Python, Data Structures, Web Dev, AI/ML)\n"
            "2. Mechanical & Civil Engineering\n"
            "3. Mathematics, Physics & Applied Sciences\n"
            "4. Management, Commerce & Business Economics\n"
            "You can use the OPAC search kiosks located on the 1st Floor to check real-time shelf status."
        )

    # Rule 8: Digital Library & E-Journals
    elif "digital" in text or "e-book" in text or "journal" in text or "ieee" in text or "wifi" in text:
        return (
            "**Digital Resource Access:**\n"
            "• Over 15,000+ e-books and national/international journals via DELNET, IEEE Xplore, and NDLI.\n"
            "• 40 dedicated high-speed PC terminals on the 2nd Floor.\n"
            "• Login credentials are provided during your library orientation."
        )

    # Rule 9: Membership & Library Card
    elif "card" in text or "membership" in text or "lost card" in text or "register" in text:
        return (
            "Every admitted student receives an RFID library card automatically during enrollment. "
            "If you have lost your card, report it immediately to the librarian. Duplicate card fee: ₹100."
        )

    # Rule 10: Quiet Hall & Study Rooms
    elif "study room" in text or "discussion" in text or "reading room" in text or "hall" in text:
        return (
            "We provide two quiet reading halls (Capacity: 300 seats) and 3 collaborative group discussion "
            "cubicles on the 3rd floor. Group rooms must be booked at least 2 hours in advance at the counter."
        )

    # Rule 11: Contact & Librarian Information
    elif "contact" in text or "librarian" in text or "email" in text or "phone" in text:
        return (
            "**Library Help Desk Contact:**\n"
            "• Email: library@gmiu.edu.in\n"
            "• Location: Central Library Building, 1st Floor\n"
            "• Circulation Counter Extension: #214"
        )

    # Rule 12: Gratitude / Courtesy
    elif "thank" in text or "thanks" in text:
        return "You're most welcome! Enjoy your reading, and let me know if you need any other library assistance."

    # Rule 13: Goodbyes & Exit
    elif text in ["bye", "exit", "quit", "see you", "goodbye"]:
        return "Goodbye! Happy reading and best of luck with your studies!"

    # Default Fallback Rule
    else:
        return (
            "I'm sorry, I couldn't locate that topic in the library rulebook. "
            "You can ask me about borrowing rules, library timings, late fines, book renewal, "
            "e-journals, or reading room facilities."
        )

# -----------------------------------------------------------------------------
# Chat Interface & Message State Management
# -----------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I am your Library Desk Bot. Ask me about books, borrowing limits, operating hours, fines, or digital journals!"
        }
    ]

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input prompt
if user_prompt := st.chat_input("Ask a library question (e.g., 'What is the fine for late return?')..."):
    # Render user prompt
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Generate response
    reply = get_library_response(user_prompt)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)