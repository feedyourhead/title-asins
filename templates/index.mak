<!DOCTYPE html>

<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Webinterpret Asin title extractor web application">
  <meta name="author" content="Daniel Wykretowicz">
  <link rel="shortcut icon" href="${request.static_url('title_asins:static/wi.ico')}">
  <link rel="stylesheet" type="text/css" href="${request.static_url('title_asins:static/base.css')}">
  <title>ASIN Translation checker</title>
</head>
<body>
  <div id="header">
    <h1>ASIN Translation checker</h1>
  </div>


  <div id="page">

    <div id="maincontent" >
      % if request.session.peek_flash():
      <div id="flash">
        <% flash = request.session.pop_flash() %>
          % for message in flash:
          ${message}<br>
          % endfor
      </div>  
      % endif
      <table>
      <tbody>
        <tr>
          <th>ASIN</th>
          <th>Original 
            % if src_site: 
            - ${src_site}
            %endif
          </th>
          <th>Translation
            % if dst_site: 
            - ${dst_site}
            %endif
          </th>    
        </tr>

        % for result in qresults['translations']:
          <tr>
            <td>
            ${result['src_asin']}
            </td>
            <td>${result['attributes']['Title']['original']}</td>
            <td>${result['attributes']['Title']['translation']}</td>    
          </tr>
        % endfor
      </tbody>
      </table>


    </div>

    <div id="nav">
      <h3></h3>
       <form method="POST" action="/">
        Enter source market:
        <br>
        ${form.select("src_site", amazon_sites)}
        <br>
        Enter destination market:
        <br>
        ${form.select("dst_site", amazon_sites)}
        <br>
        Enter Asins 
        <br/>
        ${form.textarea("src_asin", cols="35", rows="20")}
        <br/>
        <input type="submit" value="Gimme translations" />
        <br>
    </div>
    <div id="clearingdiv"></div>
  </div>
</body>
</html>