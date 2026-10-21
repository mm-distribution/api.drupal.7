# openid_test_yadis_xrds()

- **Type:** Function
- **File:** [`modules/openid/tests/openid_test.module`](_file.md), lines 92–172 · [local source](../../../../../source/modules/openid/tests/openid_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module#L92-L172)
- **Module/theme:** openid_test

## Signature

```php
function openid_test_yadis_xrds()
```

## Documentation

```text
Menu callback; XRDS document that references the OP Endpoint URL.
```

## Code

```php
function openid_test_yadis_xrds() {
  if ($_SERVER['HTTP_ACCEPT'] == 'application/xrds+xml') {
    // Only respond to XRI requests for one specific XRI. The is used to verify
    // that the XRI has been properly encoded. The "+" sign in the _xrd_r query
    // parameter is decoded to a space by PHP.
    if (arg(3) == 'xri') {
      if (variable_get('clean_url', 0)) {
        if (arg(4) != '@example*résumé;%25' || $_GET['_xrd_r'] != 'application/xrds xml') {
          drupal_not_found();
        }
      }
      else {
        // Drupal cannot properly emulate an XRI proxy resolver using unclean
        // URLs, so the arguments gets messed up.
        if (arg(4) . '/' . arg(5) != '@example*résumé;%25?_xrd_r=application/xrds xml') {
          drupal_not_found();
        }
      }
    }
    drupal_add_http_header('Content-Type', 'application/xrds+xml');
    print '<?xml version="1.0" encoding="UTF-8"?>';
    if (!empty($_GET['doctype'])) {
      print "\n<!DOCTYPE dct [ <!ELEMENT blue (#PCDATA)> ]>\n";
    }
    print '
      <xrds:XRDS xmlns:xrds="xri://$xrds" xmlns="xri://$xrd*($v*2.0)" xmlns:openid="http://openid.net/xmlns/1.0">
        <XRD>
          <Status cid="' . check_plain(variable_get('openid_test_canonical_id_status', 'verified')) . '"/>
          <ProviderID>xri://@</ProviderID>
          <CanonicalID>http://example.com/user</CanonicalID>
          <Service>
            <Type>http://example.com/this-is-ignored</Type>
          </Service>
          <Service priority="5">
            <Type>http://openid.net/signon/1.0</Type>
            <URI>http://example.com/this-is-only-openid-1.0</URI>
          </Service>
          <Service priority="10">
            <Type>http://specs.openid.net/auth/2.0/signon</Type>
            <Type>http://openid.net/srv/ax/1.0</Type>
            <URI>' . url('openid-test/endpoint', array('absolute' => TRUE)) . '</URI>
            <LocalID>http://example.com/xrds</LocalID>
          </Service>
          <Service priority="15">
            <Type>http://specs.openid.net/auth/2.0/signon</Type>
            <URI>http://example.com/this-has-too-low-priority</URI>
          </Service>
          <Service>
            <Type>http://specs.openid.net/auth/2.0/signon</Type>
            <URI>http://example.com/this-has-too-low-priority</URI>
          </Service>
          ';
    if (arg(3) == 'server') {
      print '
          <Service>
            <Type>http://specs.openid.net/auth/2.0/server</Type>
            <URI>http://example.com/this-has-too-low-priority</URI>
          </Service>
          <Service priority="20">
            <Type>http://specs.openid.net/auth/2.0/server</Type>
            <URI>' . url('openid-test/endpoint', array('absolute' => TRUE)) . '</URI>
            <LocalID>' . url('openid-test/yadis/xrds/server', array('absolute' => TRUE)) . '</LocalID>
          </Service>';
    }
    elseif (arg(3) == 'delegate') {
      print '
          <Service priority="0">
            <Type>http://specs.openid.net/auth/2.0/signon</Type>
            <Type>http://openid.net/srv/ax/1.0</Type>
            <URI>' . url('openid-test/endpoint', array('absolute' => TRUE)) . '</URI>
            <openid:Delegate>http://example.com/xrds-delegate</openid:Delegate>
          </Service>';
    }
    print '
        </XRD>
      </xrds:XRDS>';
  }
  else {
    return t('This is a regular HTML page. If the client sends an Accept: application/xrds+xml header when requesting this URL, an XRDS document is returned.');
  }
}
```

---
_Drupal 7.103 · [modules/openid/tests/openid_test.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/tests/openid_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
