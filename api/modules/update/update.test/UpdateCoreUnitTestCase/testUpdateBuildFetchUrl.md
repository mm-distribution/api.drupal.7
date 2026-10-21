# UpdateCoreUnitTestCase::testUpdateBuildFetchUrl()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 817–853 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L817-L853)
- **Class:** [UpdateCoreUnitTestCase](../UpdateCoreUnitTestCase.md)
- **Module/theme:** update

## Signature

```php
function testUpdateBuildFetchUrl()
```

## Documentation

```text
Tests that _update_build_fetch_url() builds the URL correctly.
```

## Code

```php
  function testUpdateBuildFetchUrl() {
    //first test that we didn't break the trivial case
    $project['name'] = 'update_test';
    $project['project_type'] = '';
    $project['info']['version'] = '';
    $project['info']['project status url'] = 'http://www.example.com';
    $project['includes'] = array('module1' => 'Module 1', 'module2' => 'Module 2');
    $site_key = '';
    $expected = 'http://www.example.com/' . $project['name'] . '/' . DRUPAL_CORE_COMPATIBILITY;
    $url = _update_build_fetch_url($project, $site_key);
    $this->assertEqual($url, $expected, "'$url' when no site_key provided should be '$expected'.");

    //For disabled projects it shouldn't add the site key either.
    $site_key = 'site_key';
    $project['project_type'] = 'disabled';
    $expected = 'http://www.example.com/' . $project['name'] . '/' . DRUPAL_CORE_COMPATIBILITY;
    $url = _update_build_fetch_url($project, $site_key);
    $this->assertEqual($url, $expected, "'$url' should be '$expected' for disabled projects.");

    //for enabled projects, adding the site key
    $project['project_type'] = '';
    $expected = 'http://www.example.com/' . $project['name'] . '/' . DRUPAL_CORE_COMPATIBILITY;
    $expected .= '?site_key=site_key';
    $expected .= '&list=' . rawurlencode('module1,module2');
    $url = _update_build_fetch_url($project, $site_key);
    $this->assertEqual($url, $expected, "When site_key provided, '$url' should be '$expected'.");

    // http://drupal.org/node/1481156 test incorrect logic when URL contains
    // a question mark.
    $project['info']['project status url'] = 'http://www.example.com/?project=';
    $expected = 'http://www.example.com/?project=/' . $project['name'] . '/' . DRUPAL_CORE_COMPATIBILITY;
    $expected .= '&site_key=site_key';
    $expected .= '&list=' . rawurlencode('module1,module2');
    $url = _update_build_fetch_url($project, $site_key);
    $this->assertEqual($url, $expected, "When ? is present, '$url' should be '$expected'.");

  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
