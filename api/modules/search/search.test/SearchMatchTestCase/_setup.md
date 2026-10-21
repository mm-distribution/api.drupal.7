# SearchMatchTestCase::_setup()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 44–62 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L44-L62)
- **Class:** [SearchMatchTestCase](../SearchMatchTestCase.md)
- **Module/theme:** search

## Signature

```php
function _setup()
```

## Documentation

```text
Set up a small index of items to test against.
```

## Code

```php
  function _setup() {
    variable_set('minimum_word_size', 3);

    for ($i = 1; $i <= 7; ++$i) {
      search_index($i, SEARCH_TYPE, $this->getText($i));
    }
    for ($i = 1; $i <= 5; ++$i) {
      search_index($i + 7, SEARCH_TYPE_2, $this->getText2($i));
    }
    // No getText builder function for Japanese text; just a simple array.
    foreach (array(
      13 => '以呂波耳・ほへとち。リヌルヲ。',
      14 => 'ドルーパルが大好きよ！',
      15 => 'コーヒーとケーキ',
    ) as $i => $jpn) {
      search_index($i, SEARCH_TYPE_JPN, $jpn);
    }
    search_update_totals();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
