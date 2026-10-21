# FilterUnitTestCase::testFilterXSS()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 990–1166 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L990-L1166)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testFilterXSS()
```

## Documentation

```text
Tests limiting allowed tags and XSS prevention.

XSS tests assume that script is disallowed by default and src is allowed
by default, but on* and style attributes are disallowed.

Script injection vectors mostly adopted from http://ha.ckers.org/xss.html.

Relevant CVEs:
- CVE-2002-1806, ~CVE-2005-0682, ~CVE-2005-2106, CVE-2005-3973,
  CVE-2006-1226 (= rev. 1.112?), CVE-2008-0273, CVE-2008-3740.
```

## Code

```php
  function testFilterXSS() {
    // Tag stripping, different ways to work around removal of HTML tags.
    $f = filter_xss('<script>alert(0)</script>');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping -- simple script without special characters.');

    $f = filter_xss('<script src="http://www.example.com" />');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping -- empty script with source.');

    $f = filter_xss('<ScRipt sRc=http://www.example.com/>');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- varying case.');

    $f = filter_xss("<script\nsrc\n=\nhttp://www.example.com/\n>");
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- multiline tag.');

    $f = filter_xss('<script/a src=http://www.example.com/a.js></script>');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- non whitespace character after tag name.');

    $f = filter_xss('<script/src=http://www.example.com/a.js></script>');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- no space between tag and attribute.');

    // Null between < and tag name works at least with IE6.
    $f = filter_xss("<\0scr\0ipt>alert(0)</script>");
    $this->assertNoNormalized($f, 'ipt', 'HTML tag stripping evasion -- breaking HTML with nulls.');

    $f = filter_xss("<scrscriptipt src=http://www.example.com/a.js>");
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- filter just removing "script".');

    $f = filter_xss('<<script>alert(0);//<</script>');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- double opening brackets.');

    $f = filter_xss('<script src=http://www.example.com/a.js?<b>');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- no closing tag.');

    // DRUPAL-SA-2008-047: This doesn't seem exploitable, but the filter should
    // work consistently.
    $f = filter_xss('<script>>');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- double closing tag.');

    $f = filter_xss('<script src=//www.example.com/.a>');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- no scheme or ending slash.');

    $f = filter_xss('<script src=http://www.example.com/.a');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- no closing bracket.');

    $f = filter_xss('<script src=http://www.example.com/ <');
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- opening instead of closing bracket.');

    $f = filter_xss('<nosuchtag attribute="newScriptInjectionVector">');
    $this->assertNoNormalized($f, 'nosuchtag', 'HTML tag stripping evasion -- unknown tag.');

    $f = filter_xss('<?xml:namespace ns="urn:schemas-microsoft-com:time">');
    $this->assertTrue(stripos($f, '<?xml') === FALSE, 'HTML tag stripping evasion -- starting with a question sign (processing instructions).');

    $f = filter_xss('<t:set attributeName="innerHTML" to="&lt;script defer&gt;alert(0)&lt;/script&gt;">');
    $this->assertNoNormalized($f, 't:set', 'HTML tag stripping evasion -- colon in the tag name (namespaces\' tricks).');

    $f = filter_xss('<img """><script>alert(0)</script>', array('img'));
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- a malformed image tag.');

    $f = filter_xss('<blockquote><script>alert(0)</script></blockquote>', array('blockquote'));
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- script in a blockqoute.');

    $f = filter_xss("<!--[if true]><script>alert(0)</script><![endif]-->");
    $this->assertNoNormalized($f, 'script', 'HTML tag stripping evasion -- script within a comment.');

    // Dangerous attributes removal.
    $f = filter_xss('<p onmouseover="http://www.example.com/">', array('p'));
    $this->assertNoNormalized($f, 'onmouseover', 'HTML filter attributes removal -- events, no evasion.');

    $f = filter_xss('<li style="list-style-image: url(javascript:alert(0))">', array('li'));
    $this->assertNoNormalized($f, 'style', 'HTML filter attributes removal -- style, no evasion.');

    $f = filter_xss('<img onerror   =alert(0)>', array('img'));
    $this->assertNoNormalized($f, 'onerror', 'HTML filter attributes removal evasion -- spaces before equals sign.');

    $f = filter_xss('<img onabort!#$%&()*~+-_.,:;?@[/|\]^`=alert(0)>', array('img'));
    $this->assertNoNormalized($f, 'onabort', 'HTML filter attributes removal evasion -- non alphanumeric characters before equals sign.');

    $f = filter_xss('<img oNmediAError=alert(0)>', array('img'));
    $this->assertNoNormalized($f, 'onmediaerror', 'HTML filter attributes removal evasion -- varying case.');

    // Works at least with IE6.
    $f = filter_xss("<img o\0nfocus\0=alert(0)>", array('img'));
    $this->assertNoNormalized($f, 'focus', 'HTML filter attributes removal evasion -- breaking with nulls.');

    // Only whitelisted scheme names allowed in attributes.
    $f = filter_xss('<img src="javascript:alert(0)">', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing -- no evasion.');

    $f = filter_xss('<img src=javascript:alert(0)>', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing evasion -- no quotes.');

    // A bit like CVE-2006-0070.
    $f = filter_xss('<img src="javascript:confirm(0)">', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing evasion -- no alert ;)');

    $f = filter_xss('<img src=`javascript:alert(0)`>', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing evasion -- grave accents.');

    $f = filter_xss('<img dynsrc="javascript:alert(0)">', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing -- rare attribute.');

    $f = filter_xss('<table background="javascript:alert(0)">', array('table'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing -- another tag.');

    $f = filter_xss('<base href="javascript:alert(0);//">', array('base'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing -- one more attribute and tag.');

    $f = filter_xss('<img src="jaVaSCriPt:alert(0)">', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing evasion -- varying case.');

    $f = filter_xss('<img src=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#48;&#41;>', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing evasion -- UTF-8 decimal encoding.');

    $f = filter_xss('<img src=&#00000106&#0000097&#00000118&#0000097&#00000115&#0000099&#00000114&#00000105&#00000112&#00000116&#0000058&#0000097&#00000108&#00000101&#00000114&#00000116&#0000040&#0000048&#0000041>', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing evasion -- long UTF-8 encoding.');

    $f = filter_xss('<img src=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x30&#x29>', array('img'));
    $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing evasion -- UTF-8 hex encoding.');

    $f = filter_xss("<img src=\"jav\tascript:alert(0)\">", array('img'));
    $this->assertNoNormalized($f, 'script', 'HTML scheme clearing evasion -- an embedded tab.');

    $f = filter_xss('<img src="jav&#x09;ascript:alert(0)">', array('img'));
    $this->assertNoNormalized($f, 'script', 'HTML scheme clearing evasion -- an encoded, embedded tab.');

    $f = filter_xss('<img src="jav&#x000000A;ascript:alert(0)">', array('img'));
    $this->assertNoNormalized($f, 'script', 'HTML scheme clearing evasion -- an encoded, embedded newline.');

    // With &#xD; this test would fail, but the entity gets turned into
    // &amp;#xD;, so it's OK.
    $f = filter_xss('<img src="jav&#x0D;ascript:alert(0)">', array('img'));
    $this->assertNoNormalized($f, 'script', 'HTML scheme clearing evasion -- an encoded, embedded carriage return.');

    $f = filter_xss("<img src=\"\n\n\nj\na\nva\ns\ncript:alert(0)\">", array('img'));
    $this->assertNoNormalized($f, 'cript', 'HTML scheme clearing evasion -- broken into many lines.');

    $f = filter_xss("<img src=\"jav\0a\0\0cript:alert(0)\">", array('img'));
    $this->assertNoNormalized($f, 'cript', 'HTML scheme clearing evasion -- embedded nulls.');

    // @todo This dataset currently fails under 5.4 because of
    //   https://www.drupal.org/node/1210798. Restore after it's fixed.
    if (version_compare(PHP_VERSION, '5.4.0', '<')) {
      $f = filter_xss('<img src=" &#14;  javascript:alert(0)">', array('img'));
      $this->assertNoNormalized($f, 'javascript', 'HTML scheme clearing evasion -- spaces and metacharacters before scheme.');
    }

    $f = filter_xss('<img src="vbscript:msgbox(0)">', array('img'));
    $this->assertNoNormalized($f, 'vbscript', 'HTML scheme clearing evasion -- another scheme.');

    $f = filter_xss('<img src="nosuchscheme:notice(0)">', array('img'));
    $this->assertNoNormalized($f, 'nosuchscheme', 'HTML scheme clearing evasion -- unknown scheme.');

    // Netscape 4.x javascript entities.
    $f = filter_xss('<br size="&{alert(0)}">', array('br'));
    $this->assertNoNormalized($f, 'alert', 'Netscape 4.x javascript entities.');

    // DRUPAL-SA-2008-006: Invalid UTF-8, these only work as reflected XSS with
    // Internet Explorer 6.
    $f = filter_xss("<p arg=\"\xe0\">\" style=\"background-image: url(javascript:alert(0));\"\xe0<p>", array('p'));
    $this->assertNoNormalized($f, 'style', 'HTML filter -- invalid UTF-8.');

    $f = filter_xss("\xc0aaa");
    $this->assertEqual($f, '', 'HTML filter -- overlong UTF-8 sequences.');

    $f = filter_xss("Who&#039;s Online");
    $this->assertNormalized($f, "who's online", 'HTML filter -- html entity number');

    $f = filter_xss("Who&amp;#039;s Online");
    $this->assertNormalized($f, "who&#039;s online", 'HTML filter -- encoded html entity number');

    $f = filter_xss("Who&amp;amp;#039; Online");
    $this->assertNormalized($f, "who&amp;#039; online", 'HTML filter -- double encoded html entity number');

    $f = filter_xss('<a data-a2a-url="foo">', array('a'));
    $this->assertEqual($f, '<a data-a2a-url="foo">', 'Numeric data attribute is not stripped out');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
