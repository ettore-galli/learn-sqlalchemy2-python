def render_query(session, query):
    separator = "-" * 80
    rendered = str(
        query.compile(session.get_bind(), compile_kwargs={"literal_binds": True})
        if hasattr(query, "compile")
        else query.statement.compile(
            session.get_bind(), compile_kwargs={"literal_binds": True}
        )
    )
    return f"{separator}" "\n" f"{rendered}" "\n" f"{separator}"
