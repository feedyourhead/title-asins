<!DOCTYPE html>

<html>
<head>
<link rel="stylesheet" type="text/css" href="${request.static_url('title_asins:static/base.css')}">
    <title>wi-tqa app</title>
</head>
  <body>

    <div id="header">
<h1></h1>
</div>
     <div id="nav">
     <h3>Amazon item translations finder</h3>
     <form method="POST" action="result_mako">
      Enter source market:
      <br>
      ${form.select("src_site", ["UK", "DE", "FR", "IT", "ES"])}
      <br>
      Enter destination market:
      <br>
      ${form.select("dst_site", ["DE", "UK", "FR", "IT", "ES"])}
      <br>
      Enter Asins (one term in one line), then press button below to submit.
      <br/>
      ${form.textarea("src_asin", cols="20", rows="30")}
      <br/>
      <input type="submit" value="Get translations" />
     </div>
     <div id="section" class="section">
     <%block name="section">
     </%block>
     </div>
  </body>
</html>