{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "86d71105-93df-4c74-8d61-5971797414f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  intern_name            track mentor_name\n",
      "0       Aisha     Data Science   Dr. Mehta\n",
      "1       Rahul  Web Development  Mr. Sharma\n",
      "2       Sneha     Data Science   Dr. Mehta\n",
      "3       Arjun   Cyber Security    Ms. Iyer\n"
     ]
    }
   ],
   "source": [
    "# Step 1: Import libraries\n",
    "import sqlite3\n",
    "import pandas as pd\n",
    "\n",
    "# Step 2: Create an in-memory SQLite database\n",
    "conn = sqlite3.connect(\":memory:\")\n",
    "cursor = conn.cursor()\n",
    "\n",
    "# Step 3: Create interns table\n",
    "cursor.execute(\"\"\"\n",
    "CREATE TABLE interns (\n",
    "    intern_id INTEGER PRIMARY KEY,\n",
    "    intern_name TEXT,\n",
    "    track TEXT\n",
    ")\n",
    "\"\"\")\n",
    "\n",
    "# Step 4: Create mentors table\n",
    "cursor.execute(\"\"\"\n",
    "CREATE TABLE mentors (\n",
    "    mentor_id INTEGER PRIMARY KEY,\n",
    "    mentor_name TEXT,\n",
    "    track TEXT\n",
    ")\n",
    "\"\"\")\n",
    "\n",
    "# Step 5: Insert sample data into interns\n",
    "interns_data = [\n",
    "    (1, \"Aisha\", \"Data Science\"),\n",
    "    (2, \"Rahul\", \"Web Development\"),\n",
    "    (3, \"Sneha\", \"Data Science\"),\n",
    "    (4, \"Arjun\", \"Cyber Security\")\n",
    "]\n",
    "\n",
    "cursor.executemany(\"INSERT INTO interns VALUES (?, ?, ?)\", interns_data)\n",
    "\n",
    "# Step 6: Insert sample data into mentors\n",
    "mentors_data = [\n",
    "    (101, \"Dr. Mehta\", \"Data Science\"),\n",
    "    (102, \"Mr. Sharma\", \"Web Development\"),\n",
    "    (103, \"Ms. Iyer\", \"Cyber Security\")\n",
    "]\n",
    "\n",
    "cursor.executemany(\"INSERT INTO mentors VALUES (?, ?, ?)\", mentors_data)\n",
    "\n",
    "conn.commit()\n",
    "\n",
    "# Step 7: INNER JOIN query\n",
    "query = \"\"\"\n",
    "SELECT interns.intern_name,\n",
    "       interns.track,\n",
    "       mentors.mentor_name\n",
    "FROM interns\n",
    "INNER JOIN mentors\n",
    "ON interns.track = mentors.track\n",
    "\"\"\"\n",
    "\n",
    "# Step 8: Load result into Pandas DataFrame\n",
    "df = pd.read_sql_query(query, conn)\n",
    "\n",
    "# Step 9: Display result\n",
    "print(df)\n",
    "\n",
    "# Close connection\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "56abd9a0-b4c3-4f97-8e01-cd75eb47bff9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
