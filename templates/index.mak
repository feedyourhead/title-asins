<!DOCTYPE html>

<html>
<head>
<link rel="stylesheet" type="text/css" href="${request.static_url('title_asins:static/base.css')}">
    <title>ASIN data extractor</title>
</head>
<body>
  <div id="header">
    <h1>ASIN Translation checker</h1>
  </div>
  <div id="page">
    <div id="maincontent" >
      <%block name="results">

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

        % for result in qresults:
          <tr>
            <td>${result['src_asin']}</td>
            <td>${result['original']}</td>
            <td>${result['translation']}</td>    
          </tr>
        % endfor
      </tbody>
      </table>

      </%block>
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