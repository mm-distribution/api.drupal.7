# FilterUnitTestCase::testUrlFilterContent()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1642–1664 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1642-L1664)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testUrlFilterContent()
```

## Documentation

```text
Tests URL filter on longer content.

Filters based on regular expressions should also be tested with a more
complex content than just isolated test lines.
The most common errors are:
- accidental '*' (greedy) match instead of '*?' (minimal) match.
- only matching first occurrence instead of all.
- newlines not matching '.*'.

This test covers:
- Document with multiple newlines and paragraphs (two newlines).
- Mix of several HTML tags, invalid non-HTML tags, tags to ignore and HTML
  comments.
- Empty HTML tags (BR, IMG).
- Mix of absolute and partial URLs, and e-mail addresses in one content.
- Input that exceeds PCRE backtracking limit.
```

## Code

```php
  function testUrlFilterContent() {
    // Setup dummy filter object.
    $filter = new stdClass();
    $filter->settings = array(
      'filter_url_length' => 496,
    );
    $path = drupal_get_path('module', 'filter') . '/tests';

    $input = file_get_contents($path . '/filter.url-input.txt');
    $expected = file_get_contents($path . '/filter.url-output.txt');
    $result = _filter_url($input, $filter);
    $this->assertIdentical($result, $expected, 'Complex HTML document was correctly processed.');

    // Case of a small and simple HTML document.
    $input = $expected = '<p>www.test.com</p>';
    $result = $this->filterUrlWithPcreErrors($input, $filter);
    $this->assertIdentical($expected, $result, 'Simple HTML document was left intact when PCRE errors occurred.');

    // Case of a complex HTML document.
    $input = $expected = file_get_contents($path . '/filter.url-input.txt');
    $result = $this->filterUrlWithPcreErrors($input, $filter);
    $this->assertIdentical($expected, $result, 'Complex HTML document was left intact when PCRE errors occurred.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
