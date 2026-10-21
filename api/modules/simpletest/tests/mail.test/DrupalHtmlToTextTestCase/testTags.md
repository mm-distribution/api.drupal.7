# DrupalHtmlToTextTestCase::testTags()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 223–310 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L223-L310)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testTags()
```

## Documentation

```text
Test all supported tags of drupal_html_to_text().
```

## Code

```php
  function testTags() {
    global $base_path, $base_url;
    $tests = array(
      // @todo Trailing linefeeds should be trimmed.
      '<a href = "http://drupal.org">Drupal.org</a>' => "Drupal.org [1]\n\n[1] http://drupal.org\n",
      // @todo Footer URLs should be absolute.
      "<a href = \"$base_path\">Homepage</a>" => "Homepage [1]\n\n[1] $base_url/\n",
      '<address>Drupal</address>' => "Drupal\n",
      // @todo The <address> tag is currently not supported.
      '<address>Drupal</address><address>Drupal</address>' => "DrupalDrupal\n",
      '<b>Drupal</b>' => "*Drupal*\n",
      // @todo There should be a space between the '>' and the text.
      '<blockquote>Drupal</blockquote>' => ">Drupal\n",
      '<blockquote>Drupal</blockquote><blockquote>Drupal</blockquote>' => ">Drupal\n>Drupal\n",
      '<br />Drupal<br />Drupal<br /><br />Drupal' => "Drupal\nDrupal\nDrupal\n",
      '<br/>Drupal<br/>Drupal<br/><br/>Drupal' => "Drupal\nDrupal\nDrupal\n",
      // @todo There should be two line breaks before the paragraph.
      '<br/>Drupal<br/>Drupal<br/><br/>Drupal<p>Drupal</p>' => "Drupal\nDrupal\nDrupal\nDrupal\n\n",
      '<div>Drupal</div>' => "Drupal\n",
      // @todo The <div> tag is currently not supported.
      '<div>Drupal</div><div>Drupal</div>' => "DrupalDrupal\n",
      '<em>Drupal</em>' => "/Drupal/\n",
      '<h1>Drupal</h1>' => "======== DRUPAL ==============================================================\n\n",
      '<h1>Drupal</h1><p>Drupal</p>' => "======== DRUPAL ==============================================================\n\nDrupal\n\n",
      '<h2>Drupal</h2>' => "-------- DRUPAL --------------------------------------------------------------\n\n",
      '<h2>Drupal</h2><p>Drupal</p>' => "-------- DRUPAL --------------------------------------------------------------\n\nDrupal\n\n",
      '<h3>Drupal</h3>' => ".... Drupal\n\n",
      '<h3>Drupal</h3><p>Drupal</p>' => ".... Drupal\n\nDrupal\n\n",
      '<h4>Drupal</h4>' => ".. Drupal\n\n",
      '<h4>Drupal</h4><p>Drupal</p>' => ".. Drupal\n\nDrupal\n\n",
      '<h5>Drupal</h5>' => "Drupal\n\n",
      '<h5>Drupal</h5><p>Drupal</p>' => "Drupal\n\nDrupal\n\n",
      '<h6>Drupal</h6>' => "Drupal\n\n",
      '<h6>Drupal</h6><p>Drupal</p>' => "Drupal\n\nDrupal\n\n",
      '<hr />Drupal<hr />' => "------------------------------------------------------------------------------\nDrupal\n------------------------------------------------------------------------------\n",
      '<hr/>Drupal<hr/>' => "------------------------------------------------------------------------------\nDrupal\n------------------------------------------------------------------------------\n",
      '<hr/>Drupal<hr/><p>Drupal</p>' => "------------------------------------------------------------------------------\nDrupal\n------------------------------------------------------------------------------\nDrupal\n\n",
      '<i>Drupal</i>' => "/Drupal/\n",
      '<p>Drupal</p>' => "Drupal\n\n",
      '<p>Drupal</p><p>Drupal</p>' => "Drupal\n\nDrupal\n\n",
      '<strong>Drupal</strong>' => "*Drupal*\n",
      // @todo Tables are currently not supported.
      '<table><tr><td>Drupal</td><td>Drupal</td></tr><tr><td>Drupal</td><td>Drupal</td></tr></table>' => "DrupalDrupalDrupalDrupal\n",
      '<table><tr><td>Drupal</td></tr></table><p>Drupal</p>' => "Drupal\nDrupal\n\n",
      // @todo The <u> tag is currently not supported.
      '<u>Drupal</u>' => "Drupal\n",
      '<ul><li>Drupal</li></ul>' => " * Drupal\n\n",
      '<ul><li>Drupal <em>Drupal</em> Drupal</li></ul>' => " * Drupal /Drupal/ Drupal\n\n",
      // @todo Lines containing nothing but spaces should be trimmed.
      '<ul><li>Drupal</li><li><ol><li>Drupal</li><li>Drupal</li></ol></li></ul>' => " * Drupal\n *  1) Drupal\n    2) Drupal\n   \n\n",
      '<ul><li>Drupal</li><li><ol><li>Drupal</li></ol></li><li>Drupal</li></ul>' => " * Drupal\n *  1) Drupal\n   \n * Drupal\n\n",
      '<ul><li>Drupal</li><li>Drupal</li></ul>' => " * Drupal\n * Drupal\n\n",
      '<ul><li>Drupal</li></ul><p>Drupal</p>' => " * Drupal\n\nDrupal\n\n",
      '<ol><li>Drupal</li></ol>' => " 1) Drupal\n\n",
      '<ol><li>Drupal</li><li><ul><li>Drupal</li><li>Drupal</li></ul></li></ol>' => " 1) Drupal\n 2)  * Drupal\n     * Drupal\n    \n\n",
      '<ol><li>Drupal</li><li>Drupal</li></ol>' => " 1) Drupal\n 2) Drupal\n\n",
      '<ol>Drupal</ol>' => "Drupal\n\n",
      '<ol><li>Drupal</li></ol><p>Drupal</p>' => " 1) Drupal\n\nDrupal\n\n",
      '<dl><dt>Drupal</dt></dl>' => "Drupal\n\n",
      '<dl><dt>Drupal</dt><dd>Drupal</dd></dl>' => "Drupal\n    Drupal\n\n",
      '<dl><dt>Drupal</dt><dd>Drupal</dd><dt>Drupal</dt><dd>Drupal</dd></dl>' => "Drupal\n    Drupal\nDrupal\n    Drupal\n\n",
      '<dl><dt>Drupal</dt><dd>Drupal</dd></dl><p>Drupal</p>' => "Drupal\n    Drupal\n\nDrupal\n\n",
      '<dl><dt>Drupal<dd>Drupal</dl>' => "Drupal\n    Drupal\n\n",
      '<dl><dt>Drupal</dt></dl><p>Drupal</p>' => "Drupal\n\nDrupal\n\n",
      // @todo Again, lines containing only spaces should be trimmed.
      '<ul><li>Drupal</li><li><dl><dt>Drupal</dt><dd>Drupal</dd><dt>Drupal</dt><dd>Drupal</dd></dl></li><li>Drupal</li></ul>' => " * Drupal\n * Drupal\n       Drupal\n   Drupal\n       Drupal\n   \n * Drupal\n\n",
      // Tests malformed HTML tags.
      '<br>Drupal<br>Drupal' => "Drupal\nDrupal\n",
      '<hr>Drupal<hr>Drupal' => "------------------------------------------------------------------------------\nDrupal\n------------------------------------------------------------------------------\nDrupal\n",
      '<ol><li>Drupal<li>Drupal</ol>' => " 1) Drupal\n 2) Drupal\n\n",
      '<ul><li>Drupal <em>Drupal</em> Drupal</ul></ul>' => " * Drupal /Drupal/ Drupal\n\n",
      '<ul><li>Drupal<li>Drupal</ol>' => " * Drupal\n * Drupal\n\n",
      '<ul><li>Drupal<li>Drupal</ul>' => " * Drupal\n * Drupal\n\n",
      '<ul>Drupal</ul>' => "Drupal\n\n",
      'Drupal</ul></ol></dl><li>Drupal' => "Drupal\n * Drupal\n",
      '<dl>Drupal</dl>' => "Drupal\n\n",
      '<dl>Drupal</dl><p>Drupal</p>' => "Drupal\n\nDrupal\n\n",
      '<dt>Drupal</dt>' => "Drupal\n",
      // Tests some unsupported HTML tags.
      '<html>Drupal</html>' => "Drupal\n",
      // @todo Perhaps the contents of <script> tags should be dropped.
      '<script type="text/javascript">Drupal</script>' => "Drupal\n",
    );

    foreach ($tests as $html => $text) {
      $this->assertHtmlToText($html, $text, 'Supported tags');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
