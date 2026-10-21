# DrupalAddHtmlHeadLinkTest::getInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3396–3402 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3396-L3402)
- **Class:** [DrupalAddHtmlHeadLinkTest](../DrupalAddHtmlHeadLinkTest.md)
- **Module/theme:** batch_test

## Signature

```php
public static function getInfo()
```

## Documentation

```text
{@inheritdoc}
```

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Add HTML head link',
      'description' => 'Test for drupal_add_html_head_link().',
      'group' => 'System',
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
