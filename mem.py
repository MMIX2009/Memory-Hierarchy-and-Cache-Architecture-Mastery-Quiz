import streamlit as st

# Title of the app
st.title("Memory Hierarchy and Cache Architecture Mastery Quiz")
st.write("Test your understanding of memory design and architecture!")

# Initialize session state variables if they don’t exist
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

# Questions and answers
quiz = [
    # Principle of Locality
    {"question": "What are the two types of locality in computer memory?",
     "options": ["Temporal and Spatial", "Random and Sequential", "Static and Dynamic", "Logical and Physical"],
     "answer": "Temporal and Spatial"},

    {"question": "Which type of locality refers to items accessed recently being accessed again soon?",
     "options": ["Spatial locality", "Temporal locality", "Sequential locality", "Parallel locality"],
     "answer": "Temporal locality"},

    {"question": "Which type of locality explains why array elements are accessed more efficiently?",
     "options": ["Temporal locality", "Spatial locality", "Random locality", "Cache locality"],
     "answer": "Spatial locality"},

    {"question": "What is the primary strategy of a memory hierarchy?",
     "options": ["Maximize latency", "Minimize cost", "Exploit locality", "Increase cache misses"],
     "answer": "Exploit locality"},

    # Memory Hierarchy Levels
    {"question": "What unit is transferred between memory hierarchy levels?",
     "options": ["Byte", "Word", "Block", "Page"],
     "answer": "Block"},

    {"question": "What term describes a successful data retrieval from an upper memory level?",
     "options": ["Miss", "Hit", "Cache fault", "Page fault"],
     "answer": "Hit"},

    {"question": "What is the ratio of hits to memory accesses called?",
     "options": ["Miss ratio", "Cache efficiency", "Hit ratio", "Memory bandwidth"],
     "answer": "Hit ratio"},

    {"question": "What occurs when required data is not in the cache?",
     "options": ["Page fault", "Cache miss", "Memory overflow", "Cache flush"],
     "answer": "Cache miss"},

    # Memory Technologies
    {"question": "Which memory type is the fastest but most expensive per GB?",
     "options": ["DRAM", "SRAM", "Flash", "Disk"],
     "answer": "SRAM"},

    {"question": "Which memory type requires periodic refreshing?",
     "options": ["SRAM", "ROM", "DRAM", "Cache"],
     "answer": "DRAM"},

    {"question": "What is the primary storage medium for long-term data on most computers?",
     "options": ["SRAM", "DRAM", "Flash", "Magnetic disk"],
     "answer": "Magnetic disk"},

    {"question": "Which memory technology stores data in a capacitor?",
     "options": ["DRAM", "SRAM", "Flash", "ROM"],
     "answer": "DRAM"},

    # DRAM Organization
    {"question": "What is the advantage of burst mode in DRAM?",
     "options": ["Increased latency", "Reduced latency for consecutive words", "More power consumption", "Faster disk access"],
     "answer": "Reduced latency for consecutive words"},

    {"question": "Which DRAM variant uses both rising and falling clock edges?",
     "options": ["DDR", "SDRAM", "QDR", "EDO"],
     "answer": "DDR"},

    {"question": "What does DDR stand for in memory technology?",
     "options": ["Direct Data Resource", "Dynamic Disk Read", "Double Data Rate", "Dual Disk RAM"],
     "answer": "Double Data Rate"},

    # Flash Storage
    {"question": "Which type of flash memory is commonly used in USB drives?",
     "options": ["NOR flash", "NAND flash", "EPROM", "DRAM"],
     "answer": "NAND flash"},

    {"question": "What term describes the wear of flash memory cells after repeated writes?",
     "options": ["Data corruption", "Write fatigue", "Wear leveling", "Cell degradation"],
     "answer": "Cell degradation"},

    {"question": "What technique mitigates wear in flash memory?",
     "options": ["Write-back", "Wear leveling", "Cache flushing", "Block allocation"],
     "answer": "Wear leveling"},

    # Cache Memory
    {"question": "What is the closest memory level to the CPU?",
     "options": ["Main memory", "Disk", "L1 cache", "L3 cache"],
     "answer": "L1 cache"},

    {"question": "What does a valid bit in cache memory indicate?",
     "options": ["Data is recently used", "Cache block contains valid data", "Cache block is dirty", "Cache block is empty"],
     "answer": "Cache block contains valid data"},

    {"question": "Which cache type maps each memory block to exactly one location?",
     "options": ["Fully associative", "Set associative", "Direct mapped", "Virtual cache"],
     "answer": "Direct mapped"},

    {"question": "What are the three main cache miss types?",
     "options": ["Temporary, Spatial, Logical", "Compulsory, Capacity, Conflict", "Instruction, Data, Virtual", "Soft, Hard, Critical"],
     "answer": "Compulsory, Capacity, Conflict"},

    # Cache Performance
    {"question": "What metric is calculated by: Hit time + Miss rate × Miss penalty?",
     "options": ["Cache hit time", "Average Memory Access Time (AMAT)", "Cache latency", "Memory bandwidth"],
     "answer": "Average Memory Access Time (AMAT)"},

    {"question": "What happens during a cache miss?",
     "options": ["CPU continues execution", "CPU pipeline stalls", "Data is flushed", "Data is overwritten"],
     "answer": "CPU pipeline stalls"},

    {"question": "Which performance factor becomes more significant as CPU speed increases?",
     "options": ["Cache hit rate", "Cache miss rate", "Memory stall time", "Pipeline depth"],
     "answer": "Memory stall time"},

    {"question": "What technique allows CPUs to execute independent instructions during cache misses?",
     "options": ["Branch prediction", "Out-of-order execution", "Prefetching", "Write-through"],
     "answer": "Out-of-order execution"},

    # Cache Organization
    {"question": "Which cache associativity allows any block to go anywhere?",
     "options": ["Direct mapped", "Set associative", "Fully associative", "Random cache"],
     "answer": "Fully associative"},

    {"question": "What determines the cache block location in direct-mapped caches?",
     "options": ["Block number modulo number of blocks", "Block size", "Cache index", "Tag bits"],
     "answer": "Block number modulo number of blocks"},

    {"question": "Which cache replacement policy selects the least-recently used block?",
     "options": ["FIFO", "LRU", "Random", "Optimal"],
     "answer": "LRU"},

    {"question": "In a set-associative cache, how many blocks are searched?",
     "options": ["One", "All blocks", "All sets", "n blocks in the set"],
     "answer": "n blocks in the set"},

    # Cache Writes
    {"question": "Which cache write policy updates both cache and main memory?",
     "options": ["Write-back", "Write-through", "Write-around", "Write-cache"],
     "answer": "Write-through"},

    {"question": "What is the primary drawback of write-through caches?",
     "options": ["Data corruption", "Higher latency", "Inconsistent data", "Increased complexity"],
     "answer": "Higher latency"},

    {"question": "What mechanism helps reduce write-through cache latency?",
     "options": ["Cache flushing", "Write buffer", "Prefetching", "Memory compaction"],
     "answer": "Write buffer"},

    # Cache Design Trade-offs
    {"question": "What happens when cache block size increases?",
     "options": ["Miss rate always decreases", "Miss penalty increases", "Latency decreases", "Cache size shrinks"],
     "answer": "Miss penalty increases"},

    {"question": "Which design decision reduces capacity misses?",
     "options": ["Increase block size", "Decrease cache size", "Increase cache size", "Increase associativity"],
     "answer": "Increase cache size"},

    {"question": "How does increased associativity affect cache performance?",
     "options": ["Increases miss rate", "Decreases hit time", "Reduces conflict misses", "Improves data locality"],
     "answer": "Reduces conflict misses"},

    {"question": "What is a potential drawback of higher associativity?",
     "options": ["Higher cache misses", "Increased hit time", "Lower memory bandwidth", "Cache pollution"],
     "answer": "Increased hit time"}
]

# Display the current question
current_question = quiz[st.session_state.question_index]
st.write(f"**Question {st.session_state.question_index + 1}: {current_question['question']}**")

# Multiple-choice options
selected_option = st.radio("Select your answer:", current_question["options"], key=f"question_{st.session_state.question_index}")

# Submit button to evaluate the selected answer
if st.button("Submit Answer") and not st.session_state.answer_submitted:
    if selected_option == current_question["answer"]:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect. The correct answer is: {current_question['answer']}")
    st.session_state.answer_submitted = True

# Next button (enabled only after an answer is submitted)
if st.session_state.answer_submitted:
    if st.button("Next Question"):
        if st.session_state.question_index < len(quiz) - 1:
            st.session_state.question_index += 1
            st.session_state.answer_submitted = False
            # Force rerun to display the next question immediately
            st.rerun()
        else:
            st.write("### Quiz Completed!")
            st.write(f"Your final score is {st.session_state.score}/{len(quiz)}")
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answer_submitted = False

st.write(f"**Current Score:** {st.session_state.score}")