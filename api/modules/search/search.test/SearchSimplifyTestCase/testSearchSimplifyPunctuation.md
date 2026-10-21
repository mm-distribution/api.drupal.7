# SearchSimplifyTestCase::testSearchSimplifyPunctuation()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1202–1214 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1202-L1214)
- **Class:** [SearchSimplifyTestCase](../SearchSimplifyTestCase.md)
- **Module/theme:** search

## Signature

```php
function testSearchSimplifyPunctuation()
```

## Documentation

```text
Tests that search_simplify() does the right thing with punctuation.
```

## Code

```php
  function testSearchSimplifyPunctuation() {
    $cases = array(
      array('20.03/94-28,876', '20039428876', 'Punctuation removed from numbers'),
      array('great...drupal--module', 'great drupal module', 'Multiple dot and dashes are word boundaries'),
      array('very_great-drupal.module', 'verygreatdrupalmodule', 'Single dot, dash, underscore are removed'),
      array('regular,punctuation;word', 'regular punctuation word', 'Punctuation is a word boundary'),
    );

    foreach ($cases as $case) {
      $out = trim(search_simplify($case[0]));
      $this->assertEqual($out, $case[1], $case[2]);
    }
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
