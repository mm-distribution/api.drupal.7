# LocaleUrlRewritingTest::testDomainNameNegotiationPort()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2722–2779 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2722-L2779)
- **Class:** [LocaleUrlRewritingTest](../LocaleUrlRewritingTest.md)
- **Module/theme:** locale

## Signature

```php
function testDomainNameNegotiationPort()
```

## Documentation

```text
Check URL rewriting when using a domain name and a non-standard port.
```

## Code

```php
  function testDomainNameNegotiationPort() {
    $language_domain = 'example.fr';
    $edit = array(
      'locale_language_negotiation_url_part' => 1,
    );
    $this->drupalPost('admin/config/regional/language/configure/url', $edit, t('Save configuration'));
    $edit = array(
      'prefix' => '',
      'domain' => $language_domain
    );
    $this->drupalPost('admin/config/regional/language/edit/fr', $edit, t('Save language'));

    // Enable domain configuration.
    variable_set('locale_language_negotiation_url_part', LOCALE_LANGUAGE_NEGOTIATION_URL_DOMAIN);

    // Reset static caching.
    drupal_static_reset('language_list');
    drupal_static_reset('language_url_outbound_alter');
    drupal_static_reset('language_url_rewrite_url');

    // In case index.php is part of the URLs, we need to adapt the asserted
    // URLs as well.
    $index_php = strpos(url('', array('absolute' => TRUE)), 'index.php') !== FALSE;

    // Remember current HTTP_HOST.
    $http_host = $_SERVER['HTTP_HOST'];

    // Fake a different port.
    $_SERVER['HTTP_HOST'] .= ':88';

    // Create an absolute French link.
    $languages = language_list();
    $language = $languages['fr'];
    $url = url('', array(
      'absolute' => TRUE,
      'language' => $language
    ));

    $expected = 'http://example.fr:88/';
    $expected .= $index_php ? 'index.php/' : '';

    $this->assertEqual($url, $expected, 'The right port is used.');

    // If we set the port explicitly in url(), it should not be overriden.
    $url = url('', array(
      'absolute' => TRUE,
      'language' => $language,
      'base_url' => $GLOBALS['base_url'] . ':90',
    ));

    $expected = 'http://example.fr:90/';
    $expected .= $index_php ? 'index.php/' : '';

    $this->assertEqual($url, $expected, 'A given port is not overriden.');

    // Restore HTTP_HOST.
    $_SERVER['HTTP_HOST'] = $http_host;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
