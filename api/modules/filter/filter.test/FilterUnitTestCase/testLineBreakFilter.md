# FilterUnitTestCase::testLineBreakFilter()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 902–976 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L902-L976)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testLineBreakFilter()
```

## Documentation

```text
Tests the line break filter.
```

## Code

```php
  function testLineBreakFilter() {
    // Setup dummy filter object.
    $filter = new stdClass();
    $filter->callback = '_filter_autop';

    // Since the line break filter naturally needs plenty of newlines in test
    // strings and expectations, we're using "\n" instead of regular newlines
    // here.
    $tests = array(
      // Single line breaks should be changed to <br /> tags, while paragraphs
      // separated with double line breaks should be enclosed with <p></p> tags.
      "aaa\nbbb\n\nccc" => array(
        "<p>aaa<br />\nbbb</p>\n<p>ccc</p>" => TRUE,
      ),
      // Skip contents of certain block tags entirely.
      "<script>aaa\nbbb\n\nccc</script>
<style>aaa\nbbb\n\nccc</style>
<pre>aaa\nbbb\n\nccc</pre>
<object>aaa\nbbb\n\nccc</object>
<iframe>aaa\nbbb\n\nccc</iframe>
<svg>aaa\nbbb\n\nccc</svg>
" => array(
        "<script>aaa\nbbb\n\nccc</script>" => TRUE,
        "<style>aaa\nbbb\n\nccc</style>" => TRUE,
        "<pre>aaa\nbbb\n\nccc</pre>" => TRUE,
        "<object>aaa\nbbb\n\nccc</object>" => TRUE,
        "<iframe>aaa\nbbb\n\nccc</iframe>" => TRUE,
        "<svg>aaa\nbbb\n\nccc</svg>" => TRUE,
      ),
      // Skip comments entirely.
      "One. <!-- comment --> Two.\n<!--\nThree.\n-->\n" => array(
        '<!-- comment -->' => TRUE,
        "<!--\nThree.\n-->" => TRUE,
      ),
      // Resulting HTML should produce matching paragraph tags.
      '<p><div>  </div></p>' => array(
        "<p>\n<div>  </div>\n</p>" => TRUE,
      ),
      '<div><p>  </p></div>' => array(
        "<div>\n</div>" => TRUE,
      ),
      '<blockquote><pre>aaa</pre></blockquote>' => array(
        "<blockquote><pre>aaa</pre></blockquote>" => TRUE,
      ),
      "<pre>aaa\nbbb\nccc</pre>\nddd\neee" => array(
        "<pre>aaa\nbbb\nccc</pre>" => TRUE,
        "<p>ddd<br />\neee</p>" => TRUE,
      ),
      // Comments remain unchanged and subsequent lines/paragraphs are
      // transformed normally.
      "aaa<!--comment-->\n\nbbb\n\nccc\n\nddd<!--comment\nwith linebreak-->\n\neee\n\nfff" => array(
        "<p>aaa</p>\n<!--comment--><p>\nbbb</p>\n<p>ccc</p>\n<p>ddd</p>" => TRUE,
        "<!--comment\nwith linebreak--><p>\neee</p>\n<p>fff</p>" => TRUE,
      ),
      // Check that a comment in a PRE will result that the text after
      // the comment, but still in PRE, is not transformed.
      "<pre>aaa\nbbb<!-- comment -->\n\nccc</pre>\nddd" => array(
        "<pre>aaa\nbbb<!-- comment -->\n\nccc</pre>" => TRUE,
      ),
      // Bug 810824, paragraphs were appearing around iframe tags.
      "<iframe>aaa</iframe>\n\n" => array(
        "<p><iframe>aaa</iframe></p>" => FALSE,
      ),
    );
    $this->assertFilteredString($filter, $tests);

    // Very long string hitting PCRE limits.
    $limit = max(ini_get('pcre.backtrack_limit'), ini_get('pcre.recursion_limit'));
    $source = $this->randomName($limit);
    $result = _filter_autop($source);
    $success = $this->assertEqual($result, '<p>' . $source . "</p>\n", 'Line break filter can process very long strings.');
    if (!$success) {
      $this->verbose("\n" . $source . "\n<hr />\n" . $result);
    }
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
