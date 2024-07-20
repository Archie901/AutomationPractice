
#Elements for the Claim Practice flow

class BusiMainPage:
    
    busi_claim_button = '//button[contains(text(),"Businesses")]'
    inpatient_button = '//button/div/p[contains(text(),"Inpatient")]'
    outpatient_button = '//button/div/p[contains(text(),"Outpatient")]'
    lvl2_subcat1 = '//button[contains(@class, "MuiButtonBase-root")][1]/div/p'
    lvl2_subcat2 = '//button[contains(@class, "MuiButtonBase-root")][2]/div/p'
    lvl2_subcat3 = '//button[contains(@class, "MuiButtonBase-root")][3]/div/p'
    lvl2_subcat4 = '//button[contains(@class, "MuiButtonBase-root")][4]/div/p'
    lvl2_subcat5 = '//button[contains(@class, "MuiButtonBase-root")][5]/div/p'
    lvl2_subcat7 = '//button[contains(@class, "MuiButtonBase-root")][7]/div/p'
    lvl2_subcats = []
    lvl2_subcats.extend((lvl2_subcat1, lvl2_subcat2, lvl2_subcat3, lvl2_subcat4, lvl2_subcat5, lvl2_subcat7))
    lvl3_type1 = '//button[contains(@class, "MuiButtonBase-root")][1]/div/p'
    lvl3_type2 = '//button[contains(@class, "MuiButtonBase-root")][2]/div/p'
    lvl3_type3 = '//button[contains(@class, "MuiButtonBase-root")][3]/div/p'
    lvl3_type4 = '//button[contains(@class, "MuiButtonBase-root")][4]/div/p'
    lvl3_type5 = '//button[contains(@class, "MuiButtonBase-root")][5]/div/p'
    lvl3_type6 = '//button[contains(@class, "MuiButtonBase-root")][6]/div/p'
    lvl3_type7 = '//button[contains(@class, "MuiButtonBase-root")][7]/div/p'
    lvl3_typesInp = []
    lvl3_typesInp.extend((lvl3_type1, lvl3_type2, lvl3_type3, lvl3_type4, lvl3_type5, lvl3_type6, lvl3_type7))
    lvl3_typesOutp = []
    lvl3_typesOutp.extend((lvl3_type1, lvl3_type2, lvl3_type3, lvl3_type4))
    continue_button1 = '//button[contains(text(), "Continue")]'
    continue_button2 = '//button[contains(text(), "Continue")]'
    search_input = '//input[@placeholder="Practice Name"]'
    found_prac1 = '//button[contains(@class, "MuiButtonBase-root")][1]/div/p'
    found_prac2 = '//button[contains(@class, "MuiButtonBase-root")][2]/div/p'
    found_prac3 = '//button[contains(@class, "MuiButtonBase-root")][3]/div/p'
    found_prac4 = '//button[contains(@class, "MuiButtonBase-root")][4]/div/p'
    found_prac5 = '//button[contains(@class, "MuiButtonBase-root")][5]/div/p'
    found_prac6 = '//button[contains(@class, "MuiButtonBase-root")][6]/div/p'
    found_prac7 = '//button[contains(@class, "MuiButtonBase-root")][7]/div/p'
    found_pracs = []
    found_pracs.extend((found_prac1, found_prac2, found_prac3, found_prac4, found_prac5, found_prac6, found_prac7))
    continue_button3 = '//button[contains(text(), "Continue")]'

class ConfirmIdentityPage:

    prac_name_input = '//input[@id="business-name"]'
    prac_ein_input = '//input[@placeholder="EIN"]'
    prac_address_input = '//input[@placeholder="Address"]'
    prac_phone_input = '//input[@id="phone-number"]'
    prac_email_input = '//input[@placeholder="mail@mail.com"]'
    prac_fax_input = '//input[@name="faxNumber"]'
    next_button1 = '//button[contains(text(), "Next")]'

class SelectServicesPage:

    found_serv1 = '//ul/li[1]/span[contains(@class, "MuiButtonBase-root")]'
    found_serv2 = '//ul/li[2]/span[contains(@class, "MuiButtonBase-root")]'
    found_serv3 = '//ul/li[3]/span[contains(@class, "MuiButtonBase-root")]'
    found_serv4 = '//ul/li[4]/span[contains(@class, "MuiButtonBase-root")]'
    found_serv5 = '//ul/li[5]/span[contains(@class, "MuiButtonBase-root")]'
    services_list = []
    services_list.extend((found_serv1, found_serv2, found_serv3, found_serv4, found_serv5))
    next_button2 = '//button[contains(text(), "Next")]'
    continue_button4 = '//button[contains(text(), "Continue")]'
    
class CreateAccountPage:

    create_acc_button = '//a[contains(text(), "Create Account")]'
    pa_firstName_input = '//input[@placeholder="First Name"]'
    pa_lastName_input = '//input[@placeholder="Last Name"]'
    pa_dob_input = '//input[@name="dateOfBirth"]'
    pa_phone_input = '//input[@name="phone"]'
    next_button3 = '//button[contains(text(), "Next")]'

class SetPasswordPage:

    pa_email_input = '//input[@name="email"]'
    pa_password_input = '//input[@name="password"]'
    create_button = '//button[contains(text(), "Create")]'
    verify_code_input = '//input[@autocomplete="one-time-code"]'
    login_button = '//a[contains(text(), "Log In")]'

class WebSidePages:
    
    accept_button = '//button[contains(text(), "I Accept")]'
    continue_button5 = '//button[contains(text(), "Continue")]'
    skip_button = '//button[contains(text(), "Skip")]'
    pm_selector = '//span[contains(text(), "Practice Management")]'
    locations_selector = '//span[contains(text(), "Locations")]'
    location_details = '//td//div/p[contains(@class, "MuiTypography-root")]'
    services_tab = '//button[contains(text(), "Services")]'
    profile_selector = '//span[contains(text(), "Profile")]'


#Elements for the Claim Provider flow

class ProvMainPage:

    prov_claim_button = '//button[contains(text(),"Providers")]'
    npi_input = '//input[@placeholder="NPI Number"]'
    search_button = '//button[contains(text(), "Search")]'
    yes_button = '//button[contains(text(), "Yes")]'

class ProvServicesPage:

    search_input = '//input[@placeholder="Search by Keywords"]'
    add_serv_button = '//button[contains(text(), "Add Services")]'
    serv_name_input = '//input[@id="service"]'
    desc_textarea = '//textarea[@id="description"]'
    save_button = '//button[contains(text(), "Save")]'
    back_button = '//button[contains(text(), "Back")]'
    add_more_button = '//button[contains(text(), "Add More")]'
    more_service1 = '//div[contains(@class, "MuiButtonBase-root")][1]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_service2 = '//div[contains(@class, "MuiButtonBase-root")][2]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_service3 = '//div[contains(@class, "MuiButtonBase-root")][3]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_service4 = '//div[contains(@class, "MuiButtonBase-root")][4]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_service5 = '//div[contains(@class, "MuiButtonBase-root")][5]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_service6 = '//div[contains(@class, "MuiButtonBase-root")][6]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_service7 = '//div[contains(@class, "MuiButtonBase-root")][7]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_service8 = '//div[contains(@class, "MuiButtonBase-root")][8]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_service9 = '//div[contains(@class, "MuiButtonBase-root")][9]//div[contains(@class, "MuiListItemIcon-root")]//span//input'
    more_services_list = []
    more_services_list.extend((more_service1, more_service2, more_service3, more_service4, more_service5,
                               more_service6, more_service7, more_service8, more_service9))
    close_button = '//button[contains(text(), "Close")]'
    continue_button1 = '//a[contains(text(), "Continue")]'

class LocInsurPages:

    location1_button = '//tbody/tr[1]/td/button[contains(@class, "MuiButtonBase-root")]'
    continue_button2 = '//button[contains(text(), "Continue")]'
    skip_button = '//button[contains(text(), "Skip")]'
    contact_email_input = '//input[@id="email"]'
    contact_phone_input = '//input[@id="phone-number"]'
    contact_fax_input = '//input[@id="fax-number"]'
    continue_button3 = '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]'
    pref_email_box = '//div/label[1]/span[contains(@class, "MuiButtonBase-root")]'
    pref_fax_box = '//div/label[2]/span[contains(@class, "MuiButtonBase-root")]'
    continue_button4 = '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]'
    continue_button5 = '//div[contains(@class, "MuiDialogActions-root")]//button[contains(text(), "Continue")]'

class VerifyIdentityPage:

    create_prov_button = '//a[contains(text(), "Create Account")]'
    prov_med_license_input = '//input[@id="medical-license-number"]'
    prov_state_license_dropdown = 'input[placeholder*="New Jersey"]'
    prov_dob_input = '//input[@name="dateOfBirth"]'
    next_button1 = '//button[contains(text(), "Next")]'

class CreatePasswordPage:

    prov_password_input = '//input[@name="password"]'
    prov_password_confirm = '//input[@name="passwordConfirmation"]'
    next_button2 = '//button[contains(text(), "Next")]'
    verify_code_input = '//input[@autocomplete="one-time-code"]'

class WorkInfoPage:

    prac_input = '//input[@id="practice-name"]'
    prac_email = '//input[@id="practice-email"]'
    next_button3 = '//button[contains(text(), "Next")]'
    login_button = '//a[contains(text(), "Log In")]'

class WebProvPages:

    accept_button = '//button[contains(text(), "I Accept")]'
    x_button = '//h2/button[contains(@class, "MuiButtonBase-root")]'
    profile_selector = '//span[contains(text(), "My Profile")]'
    insurance_tab = '//button[contains(text(), "Insurance")]'
    locations_tab = '//button[contains(text(), "Locations")]'
    location_open_tick = '//div[contains(@class, "_GroupWrapper_ur8f6_67")][2]//div[1]//div[contains(@class, "_LinkContent_1ubfi_31")]//button'