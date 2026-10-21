# DrupalWebTestCase::drupalSetContent()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 3245–3254 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L3245-L3254)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalSetContent($content, $url = 'internal:')
```

## Documentation

```text
Sets the raw HTML content. This can be useful when a page has been fetched
outside of the internal browser and assertions need to be made on the
returned page.

A good example would be when testing drupal_http_request(). After fetching
the page the content can be set and page elements can be checked to ensure
that the function worked properly.
```

## Code

```php
  protected function drupalSetContent($content, $url = 'internal:') {
    $this->content = $content;
    $this->url = $url;
    $this->plainTextContent = FALSE;
    $this->elements = FALSE;
    $this->drupalSettings = array();
    if (preg_match('/jQuery\.extend\(Drupal\.settings, (.*?)\);/', $content, $matches)) {
      $this->drupalSettings = drupal_json_decode($matches[1]);
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
