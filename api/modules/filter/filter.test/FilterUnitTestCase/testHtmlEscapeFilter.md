# FilterUnitTestCase::testHtmlEscapeFilter()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1279–1292 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1279-L1292)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testHtmlEscapeFilter()
```

## Documentation

```text
Tests the HTML escaping filter.

check_plain() is not tested here.
```

## Code

```php
  function testHtmlEscapeFilter() {
    // Setup dummy filter object.
    $filter = new stdClass();
    $filter->callback = '_filter_html_escape';

    $tests = array(
      "   One. <!-- \"comment\" --> Two'.\n<p>Three.</p>\n    " => array(
        "One. &lt;!-- &quot;comment&quot; --&gt; Two&#039;.\n&lt;p&gt;Three.&lt;/p&gt;" => TRUE,
        '   One.' => FALSE,
        "</p>\n    " => FALSE,
      ),
    );
    $this->assertFilteredString($filter, $tests);
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
