# SessionUnitTestCase::testSessionInitialization()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 873–960 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L873-L960)
- **Class:** [SessionUnitTestCase](../SessionUnitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testSessionInitialization()
```

## Documentation

```text
Unit test drupal_settings_initialize().
```

## Code

```php
  function testSessionInitialization() {
    global $base_url, $cookie_domain;

    $tests = array(
      array(
        'http_host' => 'example.com',
        'script_name' => '/index.php',
        'session_name' => 'SESSa379a6f6eeafb9a55e378c118034e275',
        'base_url' => 'http://example.com',
        'cookie_domain' => '.example.com',
      ),
      array(
        'http_host' => 'example.com',
        'script_name' => '/foo/index.php',
        'session_name' => 'SESS76f699faa11e8fbe9a70d933651df90f',
        'base_url' => 'http://example.com/foo',
        'cookie_domain' => '.example.com',
      ),
      array(
        'http_host' => 'one.two.example.com',
        'script_name' => '/index.php',
        'session_name' => 'SESSc0cc73483118b575693f5c255faeb739',
        'base_url' => 'http://one.two.example.com',
        'cookie_domain' => '.one.two.example.com',
      ),
      array(
        'http_host' => 'www.sub.example.com',
        'script_name' => '/index.php',
        'session_name' => 'SESSdc70980beaa5d571d3c9785cf9246c96',
        'base_url' => 'http://www.sub.example.com',
        'cookie_domain' => '.www.sub.example.com',
      ),
      array(
        'http_host' => 'example.com',
        'script_name' => '/foo/bar/index.php',
        'session_name' => 'SESSdbf7edcf4f2656b247021ceb4752f7f9',
        'base_url' => 'http://example.com/foo/bar',
        'cookie_domain' => '.example.com',
      ),
      array(
        'http_host' => 'www.sub.example.com',
        'script_name' => '/baz/index.php',
        'session_name' => 'SESS63543f965940db9e8a79801aa6d52423',
        'base_url' => 'http://www.sub.example.com/baz',
        'cookie_domain' => '.www.sub.example.com',
      ),
      array(
        'http_host' => 'sub.example.com',
        'script_name' => '/index.php',
        'session_name' => 'SESS005c4a974d8b94af421206f9ef34efeb',
        'base_url' => 'http://sub.example.com',
        'cookie_domain' => '.sub.example.com',
      ),
      array(
        'http_host' => 'www.example.com',
        'script_name' => '/index.php',
        'session_name' => 'SESS0e9f0e2600e4d8f26827597c5e324261',
        'base_url' => 'http://www.example.com',
        'cookie_domain' => '.www.example.com',
      ),
      array(
        'http_host' => 'www.example.com',
        'script_name' => '/foo/index.php',
        'session_name' => 'SESS0ddd0afc0bece848c840cdcd7b8ed9c9',
        'base_url' => 'http://www.example.com/foo',
        'cookie_domain' => '.www.example.com',
      ),
      array(
        'http_host' => 'www.example.com',
        'script_name' => '/bar/index.php',
        'session_name' => 'SESS22f2cd08599536cb4363fcd09e29d264',
        'base_url' => 'http://www.example.com/bar',
        'cookie_domain' => '.www.example.com',
      ),
    );

    foreach ($tests as $test) {
      $_SERVER['HTTP_HOST'] = $test['http_host'];
      $_SERVER['SCRIPT_NAME'] = $test['script_name'];
      $cookie_domain = NULL;
      $base_url = NULL;
      drupal_settings_initialize();
      $this->assertEqual(session_name(), $test['session_name'], 'Correct session_name for ' . $test['http_host'] . $test['script_name']);
      $this->assertEqual($base_url, $test['base_url'], 'Correct base_url for ' . $test['http_host'] . $test['script_name']);
      $this->assertEqual($cookie_domain, $test['cookie_domain'], 'Correct cookie_domain for ' . $test['http_host'] . $test['script_name']);
    }

  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
