# StatisticsLoggingTestCase::testLogging()

- **Type:** Method
- **File:** [`modules/statistics/statistics.test`](../_file.md), lines 90–165 · [local source](../../../../../source/modules/statistics/statistics.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test#L90-L165)
- **Class:** [StatisticsLoggingTestCase](../StatisticsLoggingTestCase.md)
- **Module/theme:** statistics

## Signature

```php
function testLogging()
```

## Documentation

```text
Verifies request logging for cached and uncached pages.
```

## Code

```php
  function testLogging() {
    $path = 'node/' . $this->node->nid;
    $expected = array(
      'title' => $this->node->title,
      'path' => $path,
    );

    // Verify logging of an uncached page.
    $this->drupalGet($path);
    $this->assertIdentical($this->drupalGetHeader('X-Drupal-Cache'), 'MISS', 'Testing an uncached page.');
    $log = db_query('SELECT * FROM {accesslog}')->fetchAll(PDO::FETCH_ASSOC);
    $this->assertTrue(is_array($log) && count($log) == 1, 'Page request was logged.');
    $this->assertEqual(array_intersect_key($log[0], $expected), $expected);
    $node_counter = statistics_get($this->node->nid);
    $this->assertIdentical($node_counter['totalcount'], '1');

    // Verify logging of a cached page.
    $this->drupalGet($path);
    $this->assertIdentical($this->drupalGetHeader('X-Drupal-Cache'), 'HIT', 'Testing a cached page.');
    $log = db_query('SELECT * FROM {accesslog}')->fetchAll(PDO::FETCH_ASSOC);
    $this->assertTrue(is_array($log) && count($log) == 2, 'Page request was logged.');
    $this->assertEqual(array_intersect_key($log[1], $expected), $expected);
    $node_counter = statistics_get($this->node->nid);
    $this->assertIdentical($node_counter['totalcount'], '2');

    // Test logging from authenticated users
    $this->drupalLogin($this->auth_user);
    $this->drupalGet($path);
    $log = db_query('SELECT * FROM {accesslog}')->fetchAll(PDO::FETCH_ASSOC);
    // Check the 6th item since login and account pages are also logged
    $this->assertTrue(is_array($log) && count($log) == 6, 'Page request was logged.');
    $this->assertEqual(array_intersect_key($log[5], $expected), $expected);
    $node_counter = statistics_get($this->node->nid);
    $this->assertIdentical($node_counter['totalcount'], '3');

    // Test that Ajax logging doesn't occur when disabled.
    $post = http_build_query(array('nid' => $this->node->nid));
    $headers = array('Content-Type' => 'application/x-www-form-urlencoded');
    global $base_url;
    $stats_path = $base_url . '/' . drupal_get_path('module', 'statistics'). '/statistics.php';
    drupal_http_request($stats_path, array('method' => 'POST', 'data' => $post, 'headers' => $headers, 'timeout' => 10000));
    $node_counter = statistics_get($this->node->nid);
    $this->assertIdentical($node_counter['totalcount'], '3', 'Page request was not counted via Ajax.');

    // Test that Ajax logging occurs when enabled.
    variable_set('statistics_count_content_views_ajax', 1);
    drupal_http_request($stats_path, array('method' => 'POST', 'data' => $post, 'headers' => $headers, 'timeout' => 10000));
    $node_counter = statistics_get($this->node->nid);
    $this->assertIdentical($node_counter['totalcount'], '4', 'Page request was counted via Ajax.');
    variable_set('statistics_count_content_views_ajax', 0);

    // Visit edit page to generate a title greater than 255.
    $path = 'node/' . $this->node->nid . '/edit';
    $expected = array(
      'title' => truncate_utf8(t('Edit Basic page') . ' ' . $this->node->title, 255),
      'path' => $path,
    );
    $this->drupalGet($path);
    $log = db_query('SELECT * FROM {accesslog}')->fetchAll(PDO::FETCH_ASSOC);
    $this->assertTrue(is_array($log) && count($log) == 7, 'Page request was logged.');
    $this->assertEqual(array_intersect_key($log[6], $expected), $expected);

    // Create a path longer than 255 characters. Drupal's .htaccess file
    // instructs Apache to test paths against the file system before routing to
    // index.php. Many file systems restrict file names to 255 characters
    // (http://en.wikipedia.org/wiki/Comparison_of_file_systems#Limits), and
    // Apache returns a 403 when testing longer file names, but the total path
    // length is not restricted.
    $long_path = $this->randomName(127) . '/' . $this->randomName(128);

    // Test that the long path is properly truncated when logged.
    $this->drupalGet($long_path);
    $log = db_query('SELECT * FROM {accesslog}')->fetchAll(PDO::FETCH_ASSOC);
    $this->assertTrue(is_array($log) && count($log) == 8, 'Page request was logged for a path over 255 characters.');
    $this->assertEqual($log[7]['path'], truncate_utf8($long_path, 255));
  }
```

---
_Drupal 7.103 · [modules/statistics/statistics.test](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.test) · Licensed GPL-2.0-or-later (see LICENSE)._
