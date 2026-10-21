# TextSummaryTestCase::testLongSentence()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 272–282 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L272-L282)
- **Class:** [TextSummaryTestCase](../TextSummaryTestCase.md)
- **Module/theme:** text

## Signature

```php
function testLongSentence()
```

## Documentation

```text
Test summary with long example.
```

## Code

```php
  function testLongSentence() {
    $text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' . // 125
            'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ' . // 108
            'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. ' . // 103
            'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'; // 110
    $expected = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ' .
                'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ' .
                'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.';
    // First three sentences add up to: 336, so add one for space and then 3 to get half-way into next word.
    $this->callTextSummary($text, $expected, NULL, 340);
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
