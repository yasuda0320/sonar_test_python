templates/xss_shared.html

<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}

xss.py

@xss.route('/insecure/no_template_engine_replace', methods =['GET'])
def no_template_engine_replace():
    param = request.args.get('param', 'not set')

    html = open('templates/xss_shared.html').read()
    response = make_response(html.replace('{{ name }}', param)) # Noncompliant: param is not sanitized
    return response

