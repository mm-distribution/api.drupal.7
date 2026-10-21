# DrupalWebTestCase::checkForMetaRefresh()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2682–2694 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2682-L2694)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function checkForMetaRefresh()
```

## Documentation

```text
Check for meta refresh tag and if found call drupalGet() recursively. This
function looks for the http-equiv attribute to be set to "Refresh"
and is case-sensitive.

@return
  Either the new page content or FALSE.
```

## Code

```php
  protected function checkForMetaRefresh() {
    if (strpos($this->drupalGetContent(), '<meta ') && $this->parse()) {
      $refresh = $this->xpath('//meta[@http-equiv="Refresh"]');
      if (!empty($refresh)) {
        // Parse the content attribute of the meta tag for the format:
        // "[delay]: URL=[page_to_redirect_to]".
        if (preg_match('/\d+;\s*URL=(?P<url>.*)/i', $refresh[0]['content'], $match)) {
          return $this->drupalGet($this->getAbsoluteUrl(decode_entities($match['url'])));
        }
      }
    }
    return FALSE;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
