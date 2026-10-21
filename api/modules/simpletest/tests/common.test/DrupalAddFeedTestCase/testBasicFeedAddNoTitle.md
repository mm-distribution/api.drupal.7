# DrupalAddFeedTestCase::testBasicFeedAddNoTitle()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3197–3251 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3197-L3251)
- **Class:** [DrupalAddFeedTestCase](../DrupalAddFeedTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBasicFeedAddNoTitle()
```

## Documentation

```text
Test drupal_add_feed() with paths, URLs, and titles.
```

## Code

```php
  function testBasicFeedAddNoTitle() {
    $path = $this->randomName(12);
    $external_url = 'http://' . $this->randomName(12) . '/' . $this->randomName(12);
    $fully_qualified_local_url = url($this->randomName(12), array('absolute' => TRUE));

    $path_for_title = $this->randomName(12);
    $external_for_title = 'http://' . $this->randomName(12) . '/' . $this->randomName(12);
    $fully_qualified_for_title = url($this->randomName(12), array('absolute' => TRUE));

    // Possible permutations of drupal_add_feed() to test.
    // - 'input_url': the path passed to drupal_add_feed(),
    // - 'output_url': the expected URL to be found in the header.
    // - 'title' == the title of the feed as passed into drupal_add_feed().
    $urls = array(
      'path without title' => array(
        'input_url' => $path,
        'output_url' => url($path, array('absolute' => TRUE)),
        'title' => '',
      ),
      'external URL without title' => array(
        'input_url' => $external_url,
        'output_url' => $external_url,
        'title' => '',
      ),
      'local URL without title' => array(
        'input_url' => $fully_qualified_local_url,
        'output_url' => $fully_qualified_local_url,
        'title' => '',
      ),
      'path with title' => array(
        'input_url' => $path_for_title,
        'output_url' => url($path_for_title, array('absolute' => TRUE)),
        'title' => $this->randomName(12),
      ),
      'external URL with title' => array(
        'input_url' => $external_for_title,
        'output_url' => $external_for_title,
        'title' => $this->randomName(12),
      ),
      'local URL with title' => array(
        'input_url' => $fully_qualified_for_title,
        'output_url' => $fully_qualified_for_title,
        'title' => $this->randomName(12),
      ),
    );

    foreach ($urls as $description => $feed_info) {
      drupal_add_feed($feed_info['input_url'], $feed_info['title']);
    }

    $this->drupalSetContent(drupal_get_html_head());
    foreach ($urls as $description => $feed_info) {
      $this->assertPattern($this->urlToRSSLinkPattern($feed_info['output_url'], $feed_info['title']), format_string('Found correct feed header for %description', array('%description' => $description)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
