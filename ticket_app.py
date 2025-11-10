{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8b7bc363-3945-404f-83ac-7c6babb635f2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from ticket_agent import process_ticket\n",
    "\n",
    "# Load tickets CSV\n",
    "tickets_df = pd.read_csv(\"tickets.csv\")\n",
    "\n",
    "# Apply AI agent to each ticket\n",
    "results = tickets_df[\"customer_message\"].apply(process_ticket)\n",
    "tickets_df[\"category\"] = results.apply(lambda x: x[\"category\"])\n",
    "tickets_df[\"priority\"] = results.apply(lambda x: x[\"priority\"])\n",
    "tickets_df[\"suggested_response\"] = results.apply(lambda x: x[\"suggested_response\"])\n",
    "\n",
    "# Save to a new CSV\n",
    "tickets_df.to_csv(\"tickets_processed.csv\", index=False)\n",
    "\n",
    "print(\"Tickets processed! Saved to tickets_processed.csv\")\n",
    "print(tickets_df.head())\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
