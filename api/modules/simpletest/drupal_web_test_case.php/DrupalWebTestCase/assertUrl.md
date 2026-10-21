# DrupalWebTestCase::assertUrl()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3278–3286 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3278-L3286)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function assertUrl($path, array $options = array(), $message = '', $group = 'Other')
```

## Documentation

```text
Pass if the internal browser's URL matches the given path.

@param $path
  The expected system path.
@param $options
  (optional) Any additional options to pass for $path to url().
@param $message
  Message to display.
@param $group
  The group this message belongs to, defaults to 'Other'.

@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  protected function assertUrl($path, array $options = array(), $message = '', $group = 'Other') {
    if (!$message) {
      $message = t('Current URL is @url.', array(
        '@url' => var_export(url($path, $options), TRUE),
      ));
    }
    $options['absolute'] = TRUE;
    return $this->assertEqual($this->getUrl(), url($path, $options), $message, $group);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
