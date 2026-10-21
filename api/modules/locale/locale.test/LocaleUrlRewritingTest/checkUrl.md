# LocaleUrlRewritingTest::checkUrl()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2703–2717 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2703-L2717)
- **Class:** [LocaleUrlRewritingTest](../LocaleUrlRewritingTest.md)
- **Module/theme:** locale

## Signature

```php
private function checkUrl($language, $message1, $message2)
```

## Documentation

```text
Check URL rewriting for the given language.

The test is performed with a fixed URL (the default front page) to simply
check that language prefixes are not added to it and that the prefixed URL
is actually not working.

@param string $language
  The language prefix, e.g. 'es'.
@param string $message1
  Message to display in assertion that language prefixes are not added.
@param string $message2
  The message to display confirming prefixed URL is not working.
```

## Code

```php
  private function checkUrl($language, $message1, $message2) {
    $options = array('language' => $language);
    $base_path = trim(base_path(), '/');
    $rewritten_path = trim(str_replace(array('?q=', $base_path), '', url('node', $options)), '/');
    $segments = explode('/', $rewritten_path, 2);
    $prefix = $segments[0];
    $path = isset($segments[1]) ? $segments[1] : $prefix;
    // If the rewritten URL has not a language prefix we pick the right one from
    // the language object so we can always check the prefixed URL.
    if ($this->assertNotEqual($language->prefix, $prefix, $message1)) {
      $prefix = $language->prefix;
    }
    $this->drupalGet("$prefix/$path");
    $this->assertResponse(404, $message2);
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
