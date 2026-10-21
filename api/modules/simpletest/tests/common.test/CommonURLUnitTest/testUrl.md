# CommonURLUnitTest::testUrl()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 276–346 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L276-L346)
- **Class:** [CommonURLUnitTest](../CommonURLUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testUrl()
```

## Documentation

```text
Test url() with/without query, with/without fragment, absolute on/off and
assert all that works when clean URLs are on and off.
```

## Code

```php
  function testUrl() {
    global $base_url;

    foreach (array(FALSE, TRUE) as $absolute) {
      // Get the expected start of the path string.
      $base = $absolute ? $base_url . '/' : base_path();
      $absolute_string = $absolute ? 'absolute' : NULL;

      // Disable Clean URLs.
      $GLOBALS['conf']['clean_url'] = 0;

      $url = $base . '?q=node/123';
      $result = url('node/123', array('absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . '?q=node/123#foo';
      $result = url('node/123', array('fragment' => 'foo', 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . '?q=node/123&foo';
      $result = url('node/123', array('query' => array('foo' => NULL), 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . '?q=node/123&foo=bar&bar=baz';
      $result = url('node/123', array('query' => array('foo' => 'bar', 'bar' => 'baz'), 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . '?q=node/123&foo#bar';
      $result = url('node/123', array('query' => array('foo' => NULL), 'fragment' => 'bar', 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . '?q=node/123&foo#0';
      $result = url('node/123', array('query' => array('foo' => NULL), 'fragment' => '0', 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . '?q=node/123&foo';
      $result = url('node/123', array('query' => array('foo' => NULL), 'fragment' => '', 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base;
      $result = url('<front>', array('absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      // Enable Clean URLs.
      $GLOBALS['conf']['clean_url'] = 1;

      $url = $base . 'node/123';
      $result = url('node/123', array('absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . 'node/123#foo';
      $result = url('node/123', array('fragment' => 'foo', 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . 'node/123?foo';
      $result = url('node/123', array('query' => array('foo' => NULL), 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . 'node/123?foo=bar&bar=baz';
      $result = url('node/123', array('query' => array('foo' => 'bar', 'bar' => 'baz'), 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base . 'node/123?foo#bar';
      $result = url('node/123', array('query' => array('foo' => NULL), 'fragment' => 'bar', 'absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");

      $url = $base;
      $result = url('<front>', array('absolute' => $absolute));
      $this->assertEqual($url, $result, "$url == $result");
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
