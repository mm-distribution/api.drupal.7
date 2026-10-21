# FilterUnitTestCase::testHtmlCorrectorFilter()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1671–1855 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1671-L1855)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testHtmlCorrectorFilter()
```

## Documentation

```text
Tests the HTML corrector filter.

@todo This test could really use some validity checking function.
```

## Code

```php
  function testHtmlCorrectorFilter() {
    // Tag closing.
    $f = _filter_htmlcorrector('<p>text');
    $this->assertEqual($f, '<p>text</p>', 'HTML corrector -- tag closing at the end of input.');

    $f = _filter_htmlcorrector('<p>text<p><p>text');
    $this->assertEqual($f, '<p>text</p><p></p><p>text</p>', 'HTML corrector -- tag closing.');

    $f = _filter_htmlcorrector("<ul><li>e1<li>e2");
    $this->assertEqual($f, "<ul><li>e1</li><li>e2</li></ul>", 'HTML corrector -- unclosed list tags.');

    $f = _filter_htmlcorrector('<div id="d">content');
    $this->assertEqual($f, '<div id="d">content</div>', 'HTML corrector -- unclosed tag with attribute.');

    // XHTML slash for empty elements.
    $f = _filter_htmlcorrector('<hr><br>');
    $this->assertEqual($f, '<hr /><br />', 'HTML corrector -- XHTML closing slash.');

    $f = _filter_htmlcorrector('<P>test</P>');
    $this->assertEqual($f, '<p>test</p>', 'HTML corrector -- Convert uppercased tags to proper lowercased ones.');

    $f = _filter_htmlcorrector('<P>test</p>');
    $this->assertEqual($f, '<p>test</p>', 'HTML corrector -- Convert uppercased tags to proper lowercased ones.');

    $f = _filter_htmlcorrector('test<hr />');
    $this->assertEqual($f, 'test<hr />', 'HTML corrector -- Let proper XHTML pass through.');

    $f = _filter_htmlcorrector('test<hr/>');
    $this->assertEqual($f, 'test<hr />', 'HTML corrector -- Let proper XHTML pass through, but ensure there is a single space before the closing slash.');

    $f = _filter_htmlcorrector('test<hr    />');
    $this->assertEqual($f, 'test<hr />', 'HTML corrector -- Let proper XHTML pass through, but ensure there are not too many spaces before the closing slash.');

    $f = _filter_htmlcorrector('<span class="test" />');
    $this->assertEqual($f, '<span class="test"></span>', 'HTML corrector -- Convert XHTML that is properly formed but that would not be compatible with typical HTML user agents.');

    $f = _filter_htmlcorrector('test1<br class="test">test2');
    $this->assertEqual($f, 'test1<br class="test" />test2', 'HTML corrector -- Automatically close single tags.');

    $f = _filter_htmlcorrector('line1<hr>line2');
    $this->assertEqual($f, 'line1<hr />line2', 'HTML corrector -- Automatically close single tags.');

    $f = _filter_htmlcorrector('line1<HR>line2');
    $this->assertEqual($f, 'line1<hr />line2', 'HTML corrector -- Automatically close single tags.');

    $f = _filter_htmlcorrector('<img src="http://example.com/test.jpg">test</img>');
    $this->assertEqual($f, '<img src="http://example.com/test.jpg" />test', 'HTML corrector -- Automatically close single tags.');

    $f = _filter_htmlcorrector('<br></br>');
    $this->assertEqual($f, '<br />', "HTML corrector -- Transform empty tags to a single closed tag if the tag's content model is EMPTY.");

    $f = _filter_htmlcorrector('<div></div>');
    $this->assertEqual($f, '<div></div>', "HTML corrector -- Do not transform empty tags to a single closed tag if the tag's content model is not EMPTY.");

    $f = _filter_htmlcorrector('<p>line1<br/><hr/>line2</p>');
    $this->assertEqual($f, '<p>line1<br /></p><hr />line2', 'HTML corrector -- Move non-inline elements outside of inline containers.');

    $f = _filter_htmlcorrector('<p>line1<div>line2</div></p>');
    $this->assertEqual($f, '<p>line1</p><div>line2</div>', 'HTML corrector -- Move non-inline elements outside of inline containers.');

    $f = _filter_htmlcorrector('<p>test<p>test</p>\n');
    $this->assertEqual($f, '<p>test</p><p>test</p>\n', 'HTML corrector -- Auto-close improperly nested tags.');

    $f = _filter_htmlcorrector('<p>Line1<br><STRONG>bold stuff</b>');
    $this->assertEqual($f, '<p>Line1<br /><strong>bold stuff</strong></p>', 'HTML corrector -- Properly close unclosed tags, and remove useless closing tags.');

    $f = _filter_htmlcorrector('test <!-- this is a comment -->');
    $this->assertEqual($f, 'test <!-- this is a comment -->', 'HTML corrector -- Do not touch HTML comments.');

    $f = _filter_htmlcorrector('test <!--this is a comment-->');
    $this->assertEqual($f, 'test <!--this is a comment-->', 'HTML corrector -- Do not touch HTML comments.');

    $f = _filter_htmlcorrector('test <!-- comment <p>another
    <strong>multiple</strong> line
    comment</p> -->');
    $this->assertEqual($f, 'test <!-- comment <p>another
    <strong>multiple</strong> line
    comment</p> -->', 'HTML corrector -- Do not touch HTML comments.');

    $f = _filter_htmlcorrector('test <!-- comment <p>another comment</p> -->');
    $this->assertEqual($f, 'test <!-- comment <p>another comment</p> -->', 'HTML corrector -- Do not touch HTML comments.');

    $f = _filter_htmlcorrector('test <!--break-->');
    $this->assertEqual($f, 'test <!--break-->', 'HTML corrector -- Do not touch HTML comments.');

    $f = _filter_htmlcorrector('<p>test\n</p>\n');
    $this->assertEqual($f, '<p>test\n</p>\n', 'HTML corrector -- New-lines are accepted and kept as-is.');

    $f = _filter_htmlcorrector('<p>دروبال');
    $this->assertEqual($f, '<p>دروبال</p>', 'HTML corrector -- Encoding is correctly kept.');

    $f = _filter_htmlcorrector('<script type="text/javascript">alert("test")</script>');
    $this->assertEqual($f, '<script type="text/javascript">
<!--//--><![CDATA[// ><!--
alert("test")
//--><!]]>
</script>', 'HTML corrector -- CDATA added to script element');

    $f = _filter_htmlcorrector('<p><script type="text/javascript">alert("test")</script></p>');
    $this->assertEqual($f, '<p><script type="text/javascript">
<!--//--><![CDATA[// ><!--
alert("test")
//--><!]]>
</script></p>', 'HTML corrector -- CDATA added to a nested script element');

    $f = _filter_htmlcorrector('<p><style> /* Styling */ body {color:red}</style></p>');
    $this->assertEqual($f, '<p><style>
<!--/*--><![CDATA[/* ><!--*/
 /* Styling */ body {color:red}
/*--><!]]>*/
</style></p>', 'HTML corrector -- CDATA added to a style element.');

    $filtered_data = _filter_htmlcorrector('<p><style>
/*<![CDATA[*/
/* Styling */
body {color:red}
/*]]>*/
</style></p>');
    $this->assertEqual($filtered_data, '<p><style>
<!--/*--><![CDATA[/* ><!--*/

/*<![CDATA[*/
/* Styling */
body {color:red}
/*]]]]><![CDATA[>*/

/*--><!]]>*/
</style></p>',
      format_string('HTML corrector -- Existing cdata section @pattern_name properly escaped', array('@pattern_name' => '/*<![CDATA[*/'))
    );

    $filtered_data = _filter_htmlcorrector('<p><style>
  <!--/*--><![CDATA[/* ><!--*/
  /* Styling */
  body {color:red}
  /*--><!]]>*/
</style></p>');
    $this->assertEqual($filtered_data, '<p><style>
<!--/*--><![CDATA[/* ><!--*/

  <!--/*--><![CDATA[/* ><!--*/
  /* Styling */
  body {color:red}
  /*--><!]]]]><![CDATA[>*/

/*--><!]]>*/
</style></p>',
      format_string('HTML corrector -- Existing cdata section @pattern_name properly escaped', array('@pattern_name' => '<!--/*--><![CDATA[/* ><!--*/'))
    );

    $filtered_data = _filter_htmlcorrector('<p><script type="text/javascript">
<!--//--><![CDATA[// ><!--
  alert("test");
//--><!]]>
</script></p>');
    $this->assertEqual($filtered_data, '<p><script type="text/javascript">
<!--//--><![CDATA[// ><!--

<!--//--><![CDATA[// ><!--
  alert("test");
//--><!]]]]><![CDATA[>

//--><!]]>
</script></p>',
      format_string('HTML corrector -- Existing cdata section @pattern_name properly escaped', array('@pattern_name' => '<!--//--><![CDATA[// ><!--'))
    );

    $filtered_data = _filter_htmlcorrector('<p><script type="text/javascript">
// <![CDATA[
  alert("test");
// ]]>
</script></p>');
    $this->assertEqual($filtered_data, '<p><script type="text/javascript">
<!--//--><![CDATA[// ><!--

// <![CDATA[
  alert("test");
// ]]]]><![CDATA[>

//--><!]]>
</script></p>',
      format_string('HTML corrector -- Existing cdata section @pattern_name properly escaped', array('@pattern_name' => '// <![CDATA['))
    );

  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
