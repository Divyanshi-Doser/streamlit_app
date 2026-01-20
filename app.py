import streamlit as st
from PIL import Image
import webbrowser

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
page_title="Six Weeks to Save Reality",
layout="wide"
)


# ---------------- SIDEBAR ----------------
st.sidebar.title("🕒 Mission Control")
section = st.sidebar.radio(
"Jump through the timeline:",
[
"Introduction",
"Mission Timeline",
"Mission 1",
"Mission 2",
"Mission 3",
"Mission 4",
"Mission 5",
"Mission 6",
"Patterns & Learnings",
"Final Reflection"
]
)

# ---------------- Connect With Me Button On Sidebar ----------------
st.sidebar.subheader("Connect With Me 🔗")

st.pagelink("https://www.linkedin.com/in/divyanshi-doser")

st.pagelink("https://www.instagram.com/analytics_with_divyanshi")

st.pagelink("https://www.youtube.com/@AnalyticsWithDivyanshi")


    
# ---------------- INTRO ----------------
if section == "Introduction":
   
    col1, col2 = st.columns(2)
    with col1:
        img = Image.open("assets/intro.png")
        st.image(img, width=450, use_container_width=True, caption='PRESENTED BY **DIVYANSHI DOSER**', )
    col2.container(border=False,height=25)
    col2.container(border=False,height=25)
    col2.title("🚀 :red[SIX WEEKS TO SAVE REALITY] - SQL MISSION CHALLENGE")
    with col2.container(border=True, width='stretch', height='content',horizontal_alignment='center'):
            st.subheader("An Interactive SQL Storytelling Showcase")
    with col2.container(border=True, width='stretch', height='content',horizontal_alignment='center'):
        st.markdown("""
                    
      This SQL Mission Challenge is organized by :red[**Digits N Data**]
                    
      This wasn't just a series of SQL questions.
                                        
      It was a :red[**problem-solving journey**] wrapped in a :red[**sci-fi narrative**].
                    
      Over six missions, every query helped restore a fractured timeline.
      This page captures :red[**what I solved**], :red[**how I thought**], and :red[**why it mattered**].
                    
      Each mission represented a moment where the timeline could either stabilize or collapse
      and the only thing guiding those decisions was data.
                    
      This project captures not just the answers I found,
      but how I thought when the stakes kept rising.
                    
    
    """)
        
# ---------------- TIMELINE ----------------
elif section == "Mission Timeline":
    col1, col2 = st.columns(2)
    with col1:
        img = Image.open("assets/MT.png")
        st.image(img, width=450, use_container_width=True,caption='PRESENTED BY **DIVYANSHI DOSER**')
    col2.container(border=False,height=145)
    col2.container(border=False,height=45)
    col2.title("🧭 The Mission Timeline")
    with col2.container(border=True,):
        st.markdown("""
    - **Mission 1:** Understanding the chaos
    - **Mission 2:** Filtering realities
    - **Mission 3:** Sorting timelines
    - **Mission 4:** Detecting anomalies
    - **Mission 5:** Optimizing outcomes
    - **Mission 6:** The Final Jump
    """)
        st.info("💡Each mission required clarity before code. SQL was the tool - thinking was the weapon.")


# ---------------- MISSIONS ----------------
# ---------------- MISSION 1 ----------------
if section == "Mission 1":
    col1, col2 = st.columns(2)
    col2.container(border=False, height=85)
    with col1:
        img = Image.open("assets/mission1.png")
        st.image(img, width=450, use_container_width=True,caption='PRESENTED BY **DIVYANSHI DOSER**')

    with col2:
        col2.header("🔥 Mission 1 – :red[The Etheral Sign]")
        with st.container(border=True):
            st.subheader("THE CRISIS - TIMELINE INSTABILITY DETECTED")
            st.markdown("""
            **Task:**
            Find how many :red[**Active Avengers**] have a :red[**Mission Success Rate**] higher than the team average and are assigned to :red[**Primary Defense**].
            """)
        with st.container(border=True):
            st.subheader("**🧠 My Approach:**")
            st.markdown("""
    1️⃣ Calculated the :red[**Average Mission Success Rate**] for all :red[**Active Avengers**].
    
    2️⃣ :red[**Filter**] for :red[**Primary Defense**] squad  for all :red[**Active Avengers**] as the Mission Specifically Asked
                to evaluate this Frontline Group.

    3️⃣ Compared individual :red[**Active Avengers Mission Success Rate**] with Team Average.

    4️⃣ :red[**Count**] the :red[**Elite Defenders**] who matched all the criteria.

    """)
    st.subheader("**🧪 SQL Query Used:**")
    st.code("""    SELECT COUNT(AvengerID)
    FROM AvengersData
    WHERE Status = "Active"
    AND
    Assignment = "Primary Defense"
    AND
    MissionSuccessRate > (
        SELECT AVG(MissionSuccessRate)                                           
        FROM AvengersData
        WHERE Status = "Active" );""", language="sql")
    st.success("Query Executed Successfully", icon="✅")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.write("**Query Result** : ")
            st.write("**Total Active Avengers With Highest Mission Success Rate - 8 ✅**")
    with col2:
        with st.container(border=True):
            st.subheader("""
                **📖 Story Moment:**
                Stark's A.I. rebooted, half-corrupted but alive and flagged the six **Infinity Stones**.
            """)

# ---------------- MISSION 2 ----------------
elif section == "Mission 2":
    col1, col2 = st.columns(2)
    with col1:
        img = Image.open("assets/mission2.png")
        st.image(img, width=450, use_container_width=True, caption='PRESENTED BY **DIVYANSHI DOSER**')
    col2.container(border=False, height=15)
    with col2:
        st.header("🔥 Mission 2 – :red[The Displacement]")
        with st.container(border=True):
            st.subheader("THE CRISIS - STONES LOCATION DETECTED")
            st.markdown("""
                        **Task:**
                        Find the continent with the :red[**Lowest Stone Stability Index (SSI)**] - they're hidden in open, ordinary locations.
                        """)
        with st.container(border=True):
            st.subheader("**🧠 My Approach:**")
            st.markdown("""
                 1️⃣ Reviewed all Stone locations :red[**Continent-Wise**].

                 2️⃣ Compared Stability Index values.
        
                 3️⃣ Identified the continent with the :red[**Lowest SSI**] by :red[**Sorting**] them in :red[**Ascending Order**].
    
                 4️⃣ Then Flagged the most critical vulnerability zone.
             """)
        st.subheader("**🧪 SQL Query Used:**")
        st.code("""
            SELECT Continent, StabilityIndex_SSI
            FROM Stone_Locations
            ORDER BY StabilityIndex_SSI ASC
            LIMIT 1;""", language="sql")
    st.success("Query Executed Successfully", icon="✅")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.write("**Query Result** : ")
            st.write("**Continent with Lowest Stone Stability Index (SSI) - Africa ✅**")
    with col2:
        with st.container(border=True):
            st.subheader("""
                    **📖 Story Moment:**
                    Satellite scans traced the stones hidden in plain sight across four continents.
            """)


# ---------------- MISSION 3 ----------------
elif section == "Mission 3":
        col1, col2 = st.columns(2)
        with col1:
            img = Image.open("assets/mission3.png")
            st.image(img, width=450, use_container_width=True, caption='PRESENTED BY **DIVYANSHI DOSER**')

        with col2:
            st.header("🔥 Mission 3 – :red[The Rogue Agent]")
            with st.container(border=True):
                st.subheader("THE CRISIS - THE TRUTH SURFACES")
                st.markdown("""
                            **Task:**
                            Find the :red[**email address**] of the Security Officer who performed the most :red[**security sensor overrides**] within :red[**48 hours**] after :red[**Captain Marvel's**] return.
                        """)
            with st.container(border=True):
                st.subheader("**🧠 My Approach:**")
                st.markdown("""
                 1️⃣ Establish a relational :red[**Join**] between the :red[**Compound_Personnel**] and :red[**Security_Logs**] datasets using :red[**PersonnelID**].
    
                 2️⃣ Isolate records to include only those personnel identified with the :red[**'Security Officer'**] role.

                 3️⃣ :red[**Filter**] log entries to capture only actions corresponding to :red[**'Security Sensor Override'**].

                 4️⃣ Apply a time-based :red[**Filter**] to restrict data to the :red[**48-hour**] period immediately following :red[**Captain Marvel's return**].

                 5️⃣ :red[**Group**] the filtered log entries by individual :red[**Security Officer**] to consolidate their activities.

                 6️⃣ :red[**Count**] the number of :red[**'Security Sensor Override'**] incidents for each grouped officer.

                 7️⃣ :red[**Order**] the results to identify the :red[**Security Officer**] with the :red[**Highest count**] of :red[**overrides**], thus exposing the rogue agent.

                """)
        st.subheader("**🧪 SQL Query Used:**")
        st.code("""
            
        WITH Captain_Return AS (
                 SELECT  sl.Timestamp   AS  return_ts 
                 FROM  Security_Logs  AS  sl 
                 JOIN  Compound_Personnel  AS  cp 
                 ON  sl.PersonnelID  =  cp.PersonnelID 
                 WHERE  cp.Role  =  "Avenger (Captain Marvel)"
                 AND  sl.Action  =  "Return to Compound"
                )
        SELECT  cp.Name, cp.Email,  COUNT(*)  AS TotalOverrides
        FROM  Security_Logs  AS  sl 
        JOIN  Captain_Return  AS  cr
        ON  sl.Timestamp  >  cr.return_ts 
        AND  sl.Timestamp  <=  datetime(cr.return_ts,  "+48 hours")
        JOIN  Compound_Personnel  AS  cp
        ON  sl.PersonnelID  = cp.PersonnelID 
        WHERE  sl.Action  = "Security Sensor Override"
        AND  cp.Role  =  "Security Officer"
        GROUP BY   cp.Name, cp.Email
        ORDER BY  TotalOverrides  DESC 
        LIMIT 1 ;
    """, language="sql")
        st.success("Query Executed Successfully", icon="✅")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.write("**Query Result** : ")
                st.write("Email Address of Security Officer who identified as the source of the internal system overrides - **steve.coulson@shield.com** ✅")
        with col2:
            with st.container(border=True):
                st.subheader("""
                 **📖 Story Moment:**
                 Security alerts flashed: Captain Marvel brought the Stones, and someone inside betrayed the team.
                    """)
                

# ---------------- MISSION 4 ----------------
elif section == "Mission 4":
    col1, col2 = st.columns(2)
    with col1:
            img = Image.open("assets/mission4.png")
            st.image(img, width=450, use_container_width=True,caption='PRESENTED BY **DIVYANSHI DOSER**')

    with col2:
        st.container(border=False, height=23)
        st.header("🔥 Mission 4 – :red[Trace Black Market Flow]")
        with st.container(border=True):
            st.subheader("THE CRISIS - BLACK MARKET")
            st.markdown("""
                    **Task:**
                    Find the :red[**Account Holder**] Name who received the largest :red[**total transfer**] from Stark's :red[**'QUANTUM_FLOW'**] accounts in the past :red[**7 days**].
                """)
        with st.container(border=True):
            st.subheader("**🧠 My Approach:**")
            st.markdown("""
             1️⃣ Isolate all accounts designated as :red[**'QUANTUM_FLOW'**] senders within the database.
                    
             2️⃣ Apply a temporal :red[**Filter**] to include only transactions occurring within the :red[**Last 7 Days**].
                    
             3️⃣ Consolidate sender and receiver transaction records to establish complete data trails.
                    
             4️⃣ Calculate the :red[**Cumulative Sum**] of all :red[**Received Amounts**] for each :red[**Unique Account Holder**].
                    
             5️⃣ :red[**Order**] the :red[**Aggregated**] results in :red[**Descending Order**] and identify the :red[**Top Recipient**].
            """)
    st.subheader("**🧪 SQL Query Used:**")
    st.code("""
            
            SELECT ah.HolderName, SUM(st.Amount) AS total_received
            FROM
            Stark_Transactions AS st
            JOIN
            Account_Holders AS ah
            ON st.ReceiverAccount = ah.AccountID
            WHERE
            st.SenderAccount IN (
                     SELECT AccountID FROM Account_Holders
                      WHERE HolderName LIKE "%QUANTUM_FLOW%"
                    )
                AND st.TransactionDate >= (
                    SELECT DATE(MAX(TransactionDate), "-7 day")
                    )
                GROUP BY ah.HolderName
                ORDER BY total_received DESC
                LIMIT 1;
        """, language="sql")
    st.success("Query Executed Successfully", icon="✅")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.write("**Query Result** :")
            st.write("**Account Holder Name** - **Vision AI Research** ✅")
            st.write("**💸Total Transferred: 1600000**")
    with col2:
        with st.container(border=True):
            st.subheader("""
    **📖 Story Moment:**
    Data trails led to the Infinity Coalition's quantum vault under construction.
        """)
            

# ---------------- MISSION 5 ----------------
elif section == "Mission 5":
    col1,col2 = st.columns(2)
    col2.container(border=False, height=82)
    with col1:
        img = Image.open("assets/mission5.png")
        st.image(img, width=450, use_container_width=True,caption='PRESENTED BY **DIVYANSHI DOSER**')
    with col2:    
        st.header("🔥 Mission 5 – :red[The Assassin's Sequence]")
        with st.container(border=True):
            st.subheader("THE CRISIS - STOP THE ATTACK")
            st.markdown("""
                **Task:**
                From Steve's ordered :red[**movement logs (SequenceID)**], find the :red[**Timestamp (YYYY-MM-DD HH:MM:SS)**] that comes right after the location code :red[**"VIBRANIUM_SAFE"**].
            """)
        with st.container(border=True):
            st.subheader("**🧠 My Approach:**")
            st.markdown("""
                1️⃣ First, I ordered the movement logs by :red[**SequenceID**] to get the correct sequence.
                        
                2️⃣ Then, I :red[**Filtered**] rows where :red[**LocationCode**] was :red[**VIBRANIUM_SAFE**].
                        
                3️⃣ Next, I used the :red[**LEAD()**] function to look at the next row after each :red[**VIBRANIUM_SAFE**].
                        
                4️⃣ I selected the timestamp from that next row, which shows when the attack started.
                        
                5️⃣ Finally, I used :red[**LIMIT 1**] to pick the first relevant result as the mission requirement.
                """)
    with st.container(border=True):
        st.subheader("**🧪 SQL Query Used:**")
        st.code("""
            
       SELECT next_timestamp
          FROM (
            SELECT SequenceID, LocationCode,
            LEAD(TimeStamp) OVER (ORDER BY SequenceID) AS next_timestamp
            FROM Movement_Logs
                 ) t
       WHERE LocationCode = "VIBRANIUM_SAFE"
       ORDER BY SequenceID DESC
       LIMIT 1;
    """, language="sql")
    st.success("Query Executed Successfully.", icon="✅")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.write("**Query Result**: ")
            st.write("**TimeStamp** -- **2025-07-15 09:01:25 ✅**")
    with col2:
        with st.container(border=True):
            st.subheader("""
        **📖 Story Moment:**
        Sitwell's comms repeated **"VIBRANIUM_SAFE"**, the team mapped his path to intercept him.
    """)
# ---------------- MISSION 6 ----------------
elif section == "Mission 6":
    col1, col2 = st.columns(2)
    with col1:
        img = Image.open("assets/mission6.png")
        st.image(img, width=450, use_container_width=True,caption='PRESENTED BY **DIVYANSHI DOSER**')
    with col2:
        st.header("🔥 Mission 6 – :red[Chaos and The Final Jump]")
        with st.container(border=True):
            st.subheader("THE CRISIS - STRANGE HERO APPEARS")
            st.markdown("""
        **Task:**
        From the :red[**Timeline_Paradox_Simulation**] table, find the :red[**ParadoxScore**] linked to the earliest timestamp that happened on a :red[**Saturday**].
        """)
        with st.container(border=True):
            st.subheader("**🧠 My Approach:**")
            st.markdown("""
         1️⃣ First, isolated the :red[**Saturday Records**] from the dataset.
                    
         2️⃣ Then, :red[**Sorted**] by :red[**Timestamp**] in :red[**Ascending Order**].
                    
         3️⃣ If multiple rows share the same Timestamp → choose the :red[**Minimum ParadoxScore**].
        """)
    with st.container(border=True):
        st.subheader("**🧪 SQL Query Used:**")
        st.code("""
            
        SELECT ParadoxScore
        FROM Timeline_Paradox_Simulation
        WHERE DayOfWeek = 'Saturday'
        ORDER BY Timestamp ASC, ParadoxScore ASC
        LIMIT 1;
        """, language="sql")
    st.success("✅ Query Executed Successfully.")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.write("**Query Result**: ")
            st.write("ParadoxScore - **30** ✅")
    with col2:
        with st.container(border=True):
            st.subheader("""
        **📖 Story Moment:**
        Hulk held the portal.
        Ant-Man jumped into **the earliest safe timeline** where paradox was minimized.
        """)
# ---------------- PATTERNS ----------------
elif section == "Patterns & Learnings":
    col1, col2 = st.columns(2)
    col1.container(border=False, height=90)
    with col1:
        img = Image.open("assets/learnings.png")
        st.image(img, width=450, use_container_width=True,caption='PRESENTED BY **DIVYANSHI DOSER**')

    with col2:
        st.header("🔁 Patterns & Learnings")
        with st.container(border=True):
            with st.container(border=True):
                st.subheader(":blue[**Patterns I Discovered**]")
                st.markdown("""
    The questions were never about complex SQL syntax.                        
    - They were about precision.                       
    - What exactly is being asked?                        
    - What must be filtered out?                        
The story changed every time, but the discipline stayed the same:
    slow down, remove noise, and let the data speak.                        
    That realization shaped how I approached every mission that followed.
    """)  
            with st.container(border=True):
                st.subheader(":blue[**How I Approached Each Mission**]")
                st.markdown("""
    For every mission, I followed a simple but intentional process:
    - Translate the story into a clear data requirement
    - Identify the minimum conditions needed to answer correctly
    - Write queries that were readable, not clever
    - Validate the result against the story's logic not just the output
    """)
            with st.container(border=True):
                st.subheader(":blue[**Learnings**]")
                st.markdown("""
What This Challenge Taught Me-
- Most errors come from misunderstanding the question, not the query
- Simpler queries are easier to trust and explain
- Good data work is less about speed and more about clarity
- Most importantly, I learned that how you think
  matters more than the tool you use.
                    """)
# ---------------- FINAL ----------------
elif section == "Final Reflection":
    st.header("🌟 Final Reflection")
    img = Image.open("assets/reflection.png")
    st.image(img, width=450, use_container_width=True,caption='PRESENTED BY **DIVYANSHI DOSER**')
    st.container(border=False, height=55)
    st.markdown("""
    This challenge taught me that:
    - SQL is not about syntax, it's about **Thinking Clearly**.
    - Storytelling makes technical work memorable.
    - This page represents **How I think**, not just what I solved.
    - Reality didn't get saved by magic.
    It got saved by asking the right question at the right time.
    """)


