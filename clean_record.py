import core

if __name__ == "__main__":
    db_operator = core.DataBaseOperator()
    db_operator.cur.execute("delete from record_data;")
    db_operator.con.commit()
    db_operator.close()