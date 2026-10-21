# openid_help()

- **Type:** Function
- **File:** [`modules/openid/openid.module`](_file.md), lines 63–81 · [local source](../../../../source/modules/openid/openid.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module#L63-L81)
- **Module/theme:** openid
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function openid_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function openid_help($path, $arg) {
  switch ($path) {
    case 'user/%/openid':
      $output = '<p>' . t('This site supports <a href="@openid-net">OpenID</a>, a secure way to log in to many websites using a single username and password. OpenID can reduce the necessity of managing many usernames and passwords for many websites.', array('@openid-net' => 'http://openid.net')) . '</p>';
      $output .= '<p>' . t('To use OpenID you must first establish an identity on a public or private OpenID server. If you do not have an OpenID and would like one, look into one of the <a href="@openid-providers">free public providers</a>. You can find out more about OpenID at <a href="@openid-net">this website</a>.', array('@openid-providers' => 'http://openid.net/get/', '@openid-net' => 'http://openid.net')) . '</p>';
      $output .= '<p>' . t('If you already have an OpenID, enter the URL to your OpenID server below (e.g. myusername.openidprovider.com). Next time you log in, you will be able to use this URL instead of a regular username and password. You can have multiple OpenID servers if you like; just keep adding them here.') . '</p>';
      return $output;
    case 'admin/help#openid':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The OpenID module allows users to log in using the OpenID single sign on service. <a href="@openid-net">OpenID</a> is a secure method for logging into many websites with a single username and password. It does not require special software, and it does not share passwords with any site to which it is associated, including the site being logged into. The main benefit to users is that they can have a single password that they can use on many websites. This means they can easily update their single password from a centralized location, rather than having to change dozens of passwords individually. For more information, see the online handbook entry for <a href="@handbook">OpenID module</a>.', array('@openid-net' => 'http://openid.net', '@handbook' => 'http://drupal.org/documentation/modules/openid')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Logging in with OpenID') . '</dt>';
      $output .= '<dd>' . t("To log in using OpenID, a user must already have an OpenID account. Users can then create site accounts using their OpenID, assign one or more OpenIDs to an existing account, and log in using an OpenID. This lowers the barrier to registration, which helps increase the user base, and offers convenience and security to the users. Because OpenID cannot guarantee a user is legitimate, email verification is still necessary. When logging in, users are presented with the option of entering their OpenID URL, which will look like <em>myusername.openidprovider.com</em>. The site then communicates with the OpenID server, asking it to verify the identity of the user. If the user is logged into their OpenID server, the server communicates back to your site, verifying the user. If they are not logged in, the OpenID server will ask the user for their password. At no point does the site being logged into record the user's OpenID password.") . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/openid/openid.module](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.module) · Licensed GPL-2.0-or-later (see LICENSE)._
