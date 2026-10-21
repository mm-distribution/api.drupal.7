# ConfirmFormTest::assertCancelLinkUrl()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 3198–3202 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3198-L3202)
- **Class:** [ConfirmFormTest](../ConfirmFormTest.md)
- **Module/theme:** system

## Signature

```php
function assertCancelLinkUrl($url, $message = '', $group = 'Other')
```

## Documentation

```text
Asserts that a cancel link is present pointing to the provided URL.
```

## Code

```php
  function assertCancelLinkUrl($url, $message = '', $group = 'Other') {
    $links = $this->xpath('//a[normalize-space(text())=:label and @href=:url]', array(':label' => t('Cancel'), ':url' => $url));
    $message = ($message ? $message : format_string('Cancel link with url %url found.', array('%url' => $url)));
    return $this->assertTrue(isset($links[0]), $message, $group);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
