# FilterUnitTestCase::testUrlFilter()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1297–1572 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1297-L1572)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testUrlFilter()
```

## Documentation

```text
Tests the URL filter.
```

## Code

```php
  function testUrlFilter() {
    // Setup dummy filter object.
    $filter = new stdClass();
    $filter->callback = '_filter_url';
    $filter->settings = array(
      'filter_url_length' => 496,
    );
    // @todo Possible categories:
    // - absolute, mail, partial
    // - characters/encoding, surrounding markup, security

    // Create a e-mail that is too long.
    $long_email = str_repeat('a', 254) . '@example.com';
    $too_long_email = str_repeat('b', 255) . '@example.com';
    $email_with_plus_sign = 'one+two@example.com';


    // Filter selection/pattern matching.
    $tests = array(
      // HTTP URLs.
      '
http://example.com or www.example.com
' => array(
        '<a href="http://example.com">http://example.com</a>' => TRUE,
        '<a href="http://www.example.com">www.example.com</a>' => TRUE,
      ),
      // MAILTO URLs.
      '
person@example.com or mailto:person2@example.com or ' . $email_with_plus_sign . ' or ' . $long_email . ' but not ' . $too_long_email . '
' => array(
        '<a href="mailto:person@example.com">person@example.com</a>' => TRUE,
        '<a href="mailto:person2@example.com">mailto:person2@example.com</a>' => TRUE,
        '<a href="mailto:' . $long_email . '">' . $long_email . '</a>' => TRUE,
        '<a href="mailto:' . $too_long_email . '">' . $too_long_email . '</a>' => FALSE,
        '<a href="mailto:' . $email_with_plus_sign . '">' . $email_with_plus_sign . '</a>' => TRUE,
      ),
      // URI parts and special characters.
      '
http://trailingslash.com/ or www.trailingslash.com/
http://host.com/some/path?query=foo&bar[baz]=beer#fragment or www.host.com/some/path?query=foo&bar[baz]=beer#fragment
http://twitter.com/#!/example/status/22376963142324226
ftp://user:pass@ftp.example.com/~home/dir1
sftp://user@nonstandardport:222/dir
ssh://192.168.0.100/srv/git/drupal.git
' => array(
        '<a href="http://trailingslash.com/">http://trailingslash.com/</a>' => TRUE,
        '<a href="http://www.trailingslash.com/">www.trailingslash.com/</a>' => TRUE,
        '<a href="http://host.com/some/path?query=foo&amp;bar[baz]=beer#fragment">http://host.com/some/path?query=foo&amp;bar[baz]=beer#fragment</a>' => TRUE,
        '<a href="http://www.host.com/some/path?query=foo&amp;bar[baz]=beer#fragment">www.host.com/some/path?query=foo&amp;bar[baz]=beer#fragment</a>' => TRUE,
        '<a href="http://twitter.com/#!/example/status/22376963142324226">http://twitter.com/#!/example/status/22376963142324226</a>' => TRUE,
        '<a href="ftp://user:pass@ftp.example.com/~home/dir1">ftp://user:pass@ftp.example.com/~home/dir1</a>' => TRUE,
        '<a href="sftp://user@nonstandardport:222/dir">sftp://user@nonstandardport:222/dir</a>' => TRUE,
        '<a href="ssh://192.168.0.100/srv/git/drupal.git">ssh://192.168.0.100/srv/git/drupal.git</a>' => TRUE,
      ),
      // Encoding.
      '
http://ampersand.com/?a=1&b=2
http://encoded.com/?a=1&amp;b=2
' => array(
        '<a href="http://ampersand.com/?a=1&amp;b=2">http://ampersand.com/?a=1&amp;b=2</a>' => TRUE,
        '<a href="http://encoded.com/?a=1&amp;b=2">http://encoded.com/?a=1&amp;b=2</a>' => TRUE,
      ),
      // Domain name length.
      '
www.ex.ex or www.example.example or www.toolongdomainexampledomainexampledomainexampledomainexampledomain or
me@me.tv
' => array(
        '<a href="http://www.ex.ex">www.ex.ex</a>' => TRUE,
        '<a href="http://www.example.example">www.example.example</a>' => TRUE,
        'http://www.toolong' => FALSE,
        '<a href="mailto:me@me.tv">me@me.tv</a>' => TRUE,
      ),
      // Absolute URL protocols.
      // The list to test is found in the beginning of _filter_url() at
      // $protocols = variable_get('filter_allowed_protocols'... (approx line 1325).
      '
https://example.com,
ftp://ftp.example.com,
news://example.net,
telnet://example,
irc://example.host,
ssh://odd.geek,
sftp://secure.host?,
webcal://calendar,
rtsp://127.0.0.1,
not foo://disallowed.com.
' => array(
        'href="https://example.com"' => TRUE,
        'href="ftp://ftp.example.com"' => TRUE,
        'href="news://example.net"' => TRUE,
        'href="telnet://example"' => TRUE,
        'href="irc://example.host"' => TRUE,
        'href="ssh://odd.geek"' => TRUE,
        'href="sftp://secure.host"' => TRUE,
        'href="webcal://calendar"' => TRUE,
        'href="rtsp://127.0.0.1"' => TRUE,
        'href="foo://disallowed.com"' => FALSE,
        'not foo://disallowed.com.' => TRUE,
      ),
    );
    $this->assertFilteredString($filter, $tests);

    // Surrounding text/punctuation.
    $tests = array(
      '
Partial URL with trailing period www.partial.com.
E-mail with trailing comma person@example.com,
Absolute URL with trailing question http://www.absolute.com?
Query string with trailing exclamation www.query.com/index.php?a=!
Partial URL with 3 trailing www.partial.periods...
E-mail with 3 trailing exclamations@example.com!!!
Absolute URL and query string with 2 different punctuation characters (http://www.example.com/q=abc).
' => array(
        'period <a href="http://www.partial.com">www.partial.com</a>.' => TRUE,
        'comma <a href="mailto:person@example.com">person@example.com</a>,' => TRUE,
        'question <a href="http://www.absolute.com">http://www.absolute.com</a>?' => TRUE,
        'exclamation <a href="http://www.query.com/index.php?a=">www.query.com/index.php?a=</a>!' => TRUE,
        'trailing <a href="http://www.partial.periods">www.partial.periods</a>...' => TRUE,
        'trailing <a href="mailto:exclamations@example.com">exclamations@example.com</a>!!!' => TRUE,
        'characters (<a href="http://www.example.com/q=abc">http://www.example.com/q=abc</a>).' => TRUE,
      ),
      '
(www.parenthesis.com/dir?a=1&b=2#a)
' => array(
        '(<a href="http://www.parenthesis.com/dir?a=1&amp;b=2#a">www.parenthesis.com/dir?a=1&amp;b=2#a</a>)' => TRUE,
      ),
    );
    $this->assertFilteredString($filter, $tests);

    // Surrounding markup.
    $tests = array(
      '
<p xmlns="www.namespace.com" />
<p xmlns="http://namespace.com">
An <a href="http://example.com" title="Read more at www.example.info...">anchor</a>.
</p>
' => array(
        '<p xmlns="www.namespace.com" />' => TRUE,
        '<p xmlns="http://namespace.com">' => TRUE,
        'href="http://www.namespace.com"' => FALSE,
        'href="http://namespace.com"' => FALSE,
        'An <a href="http://example.com" title="Read more at www.example.info...">anchor</a>.' => TRUE,
      ),
      '
Not <a href="foo">www.relative.com</a> or <a href="http://absolute.com">www.absolute.com</a>
but <strong>http://www.strong.net</strong> or <em>www.emphasis.info</em>
' => array(
        '<a href="foo">www.relative.com</a>' => TRUE,
        'href="http://www.relative.com"' => FALSE,
        '<a href="http://absolute.com">www.absolute.com</a>' => TRUE,
        '<strong><a href="http://www.strong.net">http://www.strong.net</a></strong>' => TRUE,
        '<em><a href="http://www.emphasis.info">www.emphasis.info</a></em>' => TRUE,
      ),
      '
Test <code>using www.example.com the code tag</code>.
' => array(
        'href' => FALSE,
        'http' => FALSE,
      ),
      '
Intro.
<blockquote>
Quoted text linking to www.example.com, written by person@example.com, originating from http://origin.example.com. <code>@see www.usage.example.com or <em>www.example.info</em> bla bla</code>.
</blockquote>

Outro.
' => array(
        'href="http://www.example.com"' => TRUE,
        'href="mailto:person@example.com"' => TRUE,
        'href="http://origin.example.com"' => TRUE,
        'http://www.usage.example.com' => FALSE,
        'http://www.example.info' => FALSE,
        'Intro.' => TRUE,
        'Outro.' => TRUE,
      ),
      '
Unknown tag <x>containing x and www.example.com</x>? And a tag <pooh>beginning with p and containing www.example.pooh with p?</pooh>
' => array(
        'href="http://www.example.com"' => TRUE,
        'href="http://www.example.pooh"' => TRUE,
      ),
      '
<p>Test &lt;br/&gt;: This is a www.example17.com example <strong>with</strong> various http://www.example18.com tags. *<br/>
 It is important www.example19.com to *<br/>test different URLs and http://www.example20.com in the same paragraph. *<br>
HTML www.example21.com soup by person@example22.com can litererally http://www.example23.com contain *img*<img> anything. Just a www.example24.com with http://www.example25.com thrown in. www.example26.com from person@example27.com with extra http://www.example28.com.
' => array(
        'href="http://www.example17.com"' => TRUE,
        'href="http://www.example18.com"' => TRUE,
        'href="http://www.example19.com"' => TRUE,
        'href="http://www.example20.com"' => TRUE,
        'href="http://www.example21.com"' => TRUE,
        'href="mailto:person@example22.com"' => TRUE,
        'href="http://www.example23.com"' => TRUE,
        'href="http://www.example24.com"' => TRUE,
        'href="http://www.example25.com"' => TRUE,
        'href="http://www.example26.com"' => TRUE,
        'href="mailto:person@example27.com"' => TRUE,
        'href="http://www.example28.com"' => TRUE,
      ),
      '
<script>
<!--
  // @see www.example.com
  var exampleurl = "http://example.net";
-->
<!--//--><![CDATA[//><!--
  // @see www.example.com
  var exampleurl = "http://example.net";
//--><!]]>
</script>
' => array(
        'href="http://www.example.com"' => FALSE,
        'href="http://example.net"' => FALSE,
      ),
      '
<style>body {
  background: url(http://example.com/pixel.gif);
}</style>
' => array(
        'href' => FALSE,
      ),
      '
<!-- Skip any URLs like www.example.com in comments -->
' => array(
        'href' => FALSE,
      ),
      '
<!-- Skip any URLs like
www.example.com with a newline in comments -->
' => array(
        'href' => FALSE,
      ),
      '
<!-- Skip any URLs like www.comment.com in comments. <p>Also ignore http://commented.out/markup.</p> -->
' => array(
        'href' => FALSE,
      ),
      '
<dl>
<dt>www.example.com</dt>
<dd>http://example.com</dd>
<dd>person@example.com</dd>
<dt>Check www.example.net</dt>
<dd>Some text around http://www.example.info by person@example.info?</dd>
</dl>
' => array(
        'href="http://www.example.com"' => TRUE,
        'href="http://example.com"' => TRUE,
        'href="mailto:person@example.com"' => TRUE,
        'href="http://www.example.net"' => TRUE,
        'href="http://www.example.info"' => TRUE,
        'href="mailto:person@example.info"' => TRUE,
      ),
      '
<div>www.div.com</div>
<ul>
<li>http://listitem.com</li>
<li class="odd">www.class.listitem.com</li>
</ul>
' => array(
        '<div><a href="http://www.div.com">www.div.com</a></div>' => TRUE,
        '<li><a href="http://listitem.com">http://listitem.com</a></li>' => TRUE,
        '<li class="odd"><a href="http://www.class.listitem.com">www.class.listitem.com</a></li>' => TRUE,
      ),
    );
    $this->assertFilteredString($filter, $tests);

    // URL trimming.
    $filter->settings['filter_url_length'] = 20;
    $tests = array(
      'www.trimmed.com/d/ff.ext?a=1&b=2#a1' => array(
        '<a href="http://www.trimmed.com/d/ff.ext?a=1&amp;b=2#a1">www.trimmed.com/d/ff...</a>' => TRUE,
      ),
    );
    $this->assertFilteredString($filter, $tests);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
