# _openid_xrds_parse()

- **Type:** Function
- **File:** [`modules/openid/openid.inc`](_file.md), lines 139–201 · [local source](../../../../source/modules/openid/openid.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc#L139-L201)
- **Module/theme:** openid

## Signature

```php
function _openid_xrds_parse($raw_xml)
```

## Documentation

```text
Parse an XRDS document.

@param $raw_xml
  A string containing the XRDS document.
@return
  An array of service entries.
```

## Code

```php
function _openid_xrds_parse($raw_xml) {
  $services = array();

  // For PHP version >= 5.2.11, we can use this function to protect against
  // malicious doctype declarations and other unexpected entity loading.
  // However, we will not rely on it, and reject any XML with a DOCTYPE.
  // libxml_disable_entity_loader() is deprecated in PHP >= 8.0.
  $disable_entity_loader = function_exists('libxml_disable_entity_loader') && PHP_VERSION_ID < 80000;
  if ($disable_entity_loader) {
    $load_entities = libxml_disable_entity_loader(TRUE);
  }

  // Load the XML into a DOM document.
  $dom = new DOMDocument();
  @$dom->loadXML($raw_xml);

  // Since DOCTYPE declarations from an untrusted source could be malicious, we
  // stop parsing here and treat the XML as invalid since XRDS documents do not
  // require, and are not expected to have, a DOCTYPE.
  if (isset($dom->doctype)) {
    return array();
  }

  // Also stop parsing if there is an unreasonably large number of tags.
  if ($dom->getElementsByTagName('*')->length > variable_get('openid_xrds_maximum_tag_count', 30000)) {
    return array();
  }

  // Parse the DOM document for the information we need.
  if ($xml = simplexml_import_dom($dom)) {
    foreach ($xml->children(OPENID_NS_XRD)->XRD as $xrd) {
      foreach ($xrd->children(OPENID_NS_XRD)->Service as $service_element) {
        $service = array(
          'priority' => $service_element->attributes()->priority ? (int)$service_element->attributes()->priority : PHP_INT_MAX,
          'types' => array(),
          'uri' => (string)$service_element->children(OPENID_NS_XRD)->URI,
          'service' => $service_element,
          'xrd' => $xrd,
        );
        foreach ($service_element->Type as $type) {
          $service['types'][] = (string)$type;
        }
        if ($service_element->children(OPENID_NS_XRD)->LocalID) {
          $service['identity'] = (string)$service_element->children(OPENID_NS_XRD)->LocalID;
        }
        elseif ($service_element->children(OPENID_NS_OPENID)->Delegate) {
          $service['identity'] = (string)$service_element->children(OPENID_NS_OPENID)->Delegate;
        }
        else {
          $service['identity'] = FALSE;
        }
        $services[] = $service;
      }
    }
  }

  // Return the LIBXML options to the previous state before returning.
  if ($disable_entity_loader) {
    libxml_disable_entity_loader($load_entities);
  }

  return $services;
}
```

---
_Drupal 7.103 · [modules/openid/openid.inc](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
