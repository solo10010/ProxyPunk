from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    if flow.client_conn.peername is None:
        return

    output = []
    output.append("=" * 80)
    output.append(f"Request: {flow.request.method} {flow.request.url}")
    output.append("-" * 80)

    # Заголовки
    for key, value in flow.request.headers.items():
        output.append(f"{key}: {value}")

    # Если есть тело и метод не GET — добавить пустую строку и тело
    if flow.request.content and flow.request.method.upper() != "GET":
        output.append("")  # перенос строки между заголовками и телом
        try:
            body_text = flow.request.get_text()
            if len(body_text) > 1000:
                output.append(body_text[:1000] + "\n<...truncated...>")
            else:
                output.append(body_text)
        except UnicodeDecodeError:
            output.append("<Binary data>")

    output.append("=" * 80 + "\n")
    print("\n".join(output), flush=True)

