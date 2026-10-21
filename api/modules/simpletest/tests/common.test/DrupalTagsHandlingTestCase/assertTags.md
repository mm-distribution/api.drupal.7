# DrupalTagsHandlingTestCase::assertTags()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 732–742 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L732-L742)
- **Class:** [DrupalTagsHandlingTestCase](../DrupalTagsHandlingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertTags($tags)
```

## Documentation

```text
Helper function: asserts that the ending array of tags is what we wanted.
```

## Code

```php
  function assertTags($tags) {
    $original = $this->validTags;
    foreach ($tags as $tag) {
      $key = array_search($tag, $original);
      $this->assertTrue($key, format_string('Make sure tag %tag shows up in the final tags array (originally %original)', array('%tag' => $tag, '%original' => $key)));
      unset($original[$key]);
    }
    foreach ($original as $leftover) {
      $this->fail(format_string('Leftover tag %leftover was left over.', array('%leftover' => $leftover)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
