# SearchNumbersTestCase::testNumberSearching()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1331–1355 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1331-L1355)
- **Class:** [SearchNumbersTestCase](../SearchNumbersTestCase.md)
- **Module/theme:** search

## Signature

```php
function testNumberSearching()
```

## Documentation

```text
Tests that all the numbers can be searched.
```

## Code

```php
  function testNumberSearching() {
    $types = array_keys($this->numbers);

    foreach ($types as $type) {
      $number = $this->numbers[$type];
      // If the number is negative, remove the - sign, because - indicates
      // "not keyword" when searching.
      $number = ltrim($number, '-');
      $node = $this->nodes[$type];

      // Verify that the node title does not appear on the search page
      // with a dummy search.
      $this->drupalPost('search/node',
        array('keys' => 'foo'),
        t('Search'));
      $this->assertNoText($node->title, $type . ': node title not shown in dummy search');

      // Verify that the node title does appear as a link on the search page
      // when searching for the number.
      $this->drupalPost('search/node',
        array('keys' => $number),
        t('Search'));
      $this->assertText($node->title, format_string('%type: node title shown (search found the node) in search for number %number.', array('%type' => $type, '%number' => $number)));
    }
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
