# DrupalWebTestCase::parse()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2235–2253 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2235-L2253)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function parse()
```

## Documentation

```text
Parse content returned from curlExec using DOM and SimpleXML.

@return
  A SimpleXMLElement or FALSE on failure.
```

## Code

```php
  protected function parse() {
    if (!$this->elements) {
      // DOM can load HTML soup. But, HTML soup can throw warnings, suppress
      // them.
      $htmlDom = new DOMDocument();
      @$htmlDom->loadHTML($this->drupalGetContent());
      if ($htmlDom) {
        $this->pass(t('Valid HTML found on "@path"', array('@path' => $this->getUrl())), t('Browser'));
        // It's much easier to work with simplexml than DOM, luckily enough
        // we can just simply import our DOM tree.
        $this->elements = simplexml_import_dom($htmlDom);
      }
    }
    if (!$this->elements) {
      $this->fail(t('Parsed page successfully.'), t('Browser'));
    }

    return $this->elements;
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
