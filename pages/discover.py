import streamlit as st
import pandas as pd
from PIL import Image
import base64
import io
import requests
from utils.translation import t

# Function to create a card with image
def create_article_card(title, summary, content, image_url=None, placeholder_size=(600, 300)):
    with st.container():
        st.markdown(f"""
        <div style="border-radius:10px; border: 1px solid #f0f0f0; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        """, unsafe_allow_html=True)
        
        # Display image if available
        if image_url:
            try:
                # You can use your own hosted images or placeholder images
                st.image(image_url, use_column_width=True)
            except:
                # If image loading fails, use a placeholder
                st.image(f"/api/placeholder/{placeholder_size[0]}/{placeholder_size[1]}", use_column_width=True)
        else:
            # Use placeholder if no image provided
            st.image(f"/api/placeholder/{placeholder_size[0]}/{placeholder_size[1]}", use_column_width=True)
        
        # Title and summary
        st.markdown(f"### {title}")
        st.markdown(f"*{summary}*")
        
        # Create a button to expand and show full content
        if st.button(f"Read More", key=f"btn_{title.replace(' ', '_')}"):
            st.markdown("---")
            st.markdown(content, unsafe_allow_html=True)
            st.markdown("---")
            if st.button("Close", key=f"close_{title.replace(' ', '_')}"):
                st.experimental_rerun()
                
        st.markdown("</div>", unsafe_allow_html=True)

def get_articles(language="en"):
    """Get articles and translate if necessary"""
    articles = [
        {
            "title": "Breast Self-Examination Guide",
            "summary": "A step-by-step guide on how to perform breast self-examinations at home",
            "content": """
            <h2>Breast Self-Exam</h2>
            <p>While it's not necessary to do a formal, five-step breast exam to practice breast self-awareness, 
            it can be an easy way to make sure you're covering all the bases.</p>
            
            <h3>Step 1: Examine your breasts in a mirror with hands on hips</h3>
            <p>Begin by looking at your breasts in the mirror with your shoulders straight and your arms on your hips.</p>
            <p>Here's what you should look for:</p>
            <ul>
                <li>Breasts that are their usual size, shape, and color</li>
                <li>Breasts that are evenly shaped without visible distortion or swelling</li>
            </ul>
            <p>If you see any of the following changes, bring them to your doctor's attention:</p>
            <ul>
                <li>Dimpling, puckering, or bulging of the skin</li>
                <li>A nipple that has changed position or an inverted nipple</li>
                <li>Redness, soreness, rash, or swelling</li>
            </ul>
            
            <h3>Step 2: Raise arms and examine your breasts</h3>
            <p>Now, raise your arms and look for the same changes.</p>
            
            <h3>Step 3: Look for signs of breast fluid</h3>
            <p>While you're at the mirror, look for any signs of fluid coming out of one or both nipples.</p>
            
            <h3>Step 4: Feel for breast lumps while lying down</h3>
            <p>Next, check for breast lumps using your right hand to feel your left breast, and then your left hand 
            to feel your right breast. Use a firm, smooth touch with the first few finger pads of your hand, 
            keeping the fingers flat and together.</p>
            
            <h3>Step 5: Feel your breasts for lumps while standing or sitting</h3>
            <p>Finally, feel your breasts while you are standing or sitting. Many women find that the easiest way 
            to feel their breasts is when their skin is wet and slippery, so they like to do this step in the shower.</p>
            
            <h3>What should you do if you find a breast lump or other change?</h3>
            <ul>
                <li><strong>Don't panic</strong> - Most breast lumps turn out to be benign (not cancerous)</li>
                <li><strong>Call your doctor</strong> - Don't hesitate if you've noticed a lump or change that is new</li>
                <li><strong>Get it checked out</strong> - Your doctor will likely order breast imaging tests</li>
                <li><strong>Make sure you get answers</strong> - It's important that your doctor explains what is causing the lump</li>
            </ul>
            """,
            "image_url": "assets/images.jpeg"  # Replace with actual image path when available
        },
        {
            "title": "Understanding Mammograms",
            "summary": "What to expect during your mammogram and why they're important",
            "content": """
            <h2>Understanding Mammograms</h2>
            <p>A mammogram is an X-ray picture of the breast. Doctors use a mammogram to look for early signs of breast cancer. 
            Regular mammograms are the best tests doctors have to find breast cancer early, sometimes up to three years 
            before it can be felt.</p>
            
            <h3>When Should You Get a Mammogram?</h3>
            <p>The United States Preventive Services Task Force recommends that women who are 50 to 74 years old and are 
            at average risk for breast cancer get a mammogram every two years. Women who are 40 to 49 years old should talk 
            to their doctor about when to start and how often to get a mammogram.</p>
            
            <h3>What to Expect During a Mammogram</h3>
            <p>You'll stand in front of a special X-ray machine. A technologist will place your breast on a plastic plate. 
            Another plate will firmly press your breast from above. The plates will flatten the breast, holding it still while 
            the X-ray is being taken. You'll feel some pressure. The steps are repeated to make a side view of the breast. 
            The other breast will be X-rayed in the same way.</p>
            
            <h3>Tips for Getting a Mammogram</h3>
            <ul>
                <li>Schedule your mammogram about a week after your menstrual period (if you still have periods)</li>
                <li>Don't wear deodorant, perfume, or powder on the day of your mammogram</li>
                <li>Wear a top with a skirt or pants instead of a dress, so you'll only need to remove your top for the exam</li>
            </ul>
            
            <h3>Getting Your Results</h3>
            <p>You should get your results within 10 days. If you don't, call to ask about them. If doctors find something 
            suspicious, you'll likely be contacted within a week to take new pictures or get other tests. But that doesn't 
            mean you have cancer. A suspicious finding may be just dense breast tissue or a cyst. Other times, the image 
            just isn't clear and needs to be retaken.</p>
            """,
            "image_url": "assets/images.jpeg"  # Replace with actual image path when available
        },
        {
            "title": "Risk Factors for Breast Cancer",
            "summary": "Understanding the factors that may increase your risk of breast cancer",
            "content": """
            <h2>Risk Factors for Breast Cancer</h2>
            <p>Doctors know that breast cancer occurs when some breast cells begin to grow abnormally. These cells divide more 
            rapidly than healthy cells and continue to accumulate, forming a lump or mass. The following factors may increase 
            your risk of breast cancer:</p>
            
            <h3>Being female</h3>
            <p>Women are much more likely than men are to develop breast cancer.</p>
            
            <h3>Increasing age</h3>
            <p>Your risk of breast cancer increases as you age.</p>
            
            <h3>Personal history of breast conditions</h3>
            <p>If you've had a breast biopsy that found lobular carcinoma in situ (LCIS) or atypical hyperplasia of the breast, 
            you have an increased risk of breast cancer.</p>
            
            <h3>Personal history of breast cancer</h3>
            <p>If you've had breast cancer in one breast, you have an increased risk of developing cancer in the other breast.</p>
            
            <h3>Family history of breast cancer</h3>
            <p>If your mother, sister or daughter was diagnosed with breast cancer, particularly at a young age, your risk of 
            breast cancer is increased. Still, the majority of people diagnosed with breast cancer have no family history of the disease.</p>
            
            <h3>Inherited genes that increase cancer risk</h3>
            <p>Certain gene mutations that increase the risk of breast cancer can be passed from parents to children. The most 
            well-known gene mutations are referred to as BRCA1 and BRCA2.</p>
            
            <h3>Radiation exposure</h3>
            <p>If you received radiation treatments to your chest as a child or young adult, your risk of breast cancer is increased.</p>
            
            <h3>Obesity</h3>
            <p>Being obese increases your risk of breast cancer.</p>
            
            <h3>Beginning your period at a younger age</h3>
            <p>Beginning your period before age 12 increases your risk of breast cancer.</p>
            
            <h3>Beginning menopause at an older age</h3>
            <p>If you began menopause at an older age, you're more likely to develop breast cancer.</p>
            
            <h3>Postmenopausal hormone therapy</h3>
            <p>Women who take hormone therapy medications that combine estrogen and progesterone to treat the signs and symptoms 
            of menopause have an increased risk of breast cancer.</p>
            
            <h3>Drinking alcohol</h3>
            <p>Drinking alcohol increases the risk of breast cancer.</p>
            """,
            "image_url": "assets/images.jpeg"  # Replace with actual image path when available
        },
        {
            "title": "Early Signs and Symptoms of Breast Cancer",
            "summary": "Recognizing the warning signs that shouldn't be ignored",
            "content": """
            <h2>Early Signs and Symptoms of Breast Cancer</h2>
            <p>Being familiar with how your breasts normally look and feel can help you notice symptoms such as lumps, pain, 
            or changes in size that may be of concern. These could include:</p>
            
            <h3>A change in the size, shape or contour of your breast</h3>
            <p>If your breast looks larger or has a different shape than usual, or if the breast is not shaped the same as your 
            other breast, this might be a sign that needs checking.</p>
            
            <h3>A lump or thickening in or near your breast or in your underarm that persists through your menstrual cycle</h3>
            <p>Many women have breast lumps or thickening that turn out to be normal, but it's important to have any lump checked 
            by a healthcare provider.</p>
            
            <h3>A change in the feel or appearance of your skin on your breast or nipple</h3>
            <p>Look for dimpling, puckering, scaliness, or new creases.</p>
            
            <h3>A bloody or clear fluid discharge from your nipple</h3>
            <p>Fluid leaking from your nipple when you're not breastfeeding needs to be evaluated.</p>
            
            <h3>Redness of your breast skin</h3>
            <p>Redness on the skin of your breast or your nipple could be a sign of infection or inflammation, which may be related 
            to breast cancer in some cases.</p>
            
            <h3>A marble-like hardened area under your skin</h3>
            <p>This type of change could indicate advanced breast cancer.</p>
            
            <h3>A change in your nipple</h3>
            <p>If your nipple turns inward, or appears different in any way (flattened, pulling to one side, or changed direction), 
            or if you develop a rash or scaling on the nipple, these changes need to be checked.</p>
            
            <h3>Pain in your breast</h3>
            <p>Although most breast pain is not caused by cancer, persistent pain in one area needs to be evaluated.</p>
            
            <h3>When to see a doctor</h3>
            <p>If you find a lump or other change in your breast — even if a recent mammogram was normal — make an appointment with 
            your doctor for prompt evaluation.</p>
            """,
            "image_url": "/api/placeholder/600/300"  # Replace with actual image path when available
        },
        {
            "title": "Healthy Lifestyle Choices to Reduce Breast Cancer Risk",
            "summary": "Steps you can take to lower your risk of developing breast cancer",
            "content": """
            <h2>Healthy Lifestyle Choices to Reduce Breast Cancer Risk</h2>
            <p>Making changes in your daily life may help reduce your risk of breast cancer. Try to:</p>
            
            <h3>Maintain a healthy weight</h3>
            <p>If your weight is healthy, work to maintain that weight. If you need to lose weight, ask your doctor about 
            healthy strategies to accomplish this. Reduce the number of calories you eat each day and slowly increase the 
            amount of exercise.</p>
            
            <h3>Be physically active</h3>
            <p>Physical activity can help you maintain a healthy weight, which helps prevent breast cancer. Most healthy 
            adults should aim for at least 150 minutes a week of moderate aerobic activity or 75 minutes of vigorous aerobic 
            activity weekly, plus strength training at least twice a week.</p>
            
            <h3>Limit alcohol</h3>
            <p>The more alcohol you drink, the greater your risk of developing breast cancer. If you choose to drink alcohol, 
            limit yourself to no more than one drink a day, as even small amounts increase risk.</p>
            
            <h3>Breastfeed</h3>
            <p>Breastfeeding might play a role in breast cancer prevention. The longer you breastfeed, the greater the protective 
            effect.</p>
            
            <h3>Limit postmenopausal hormone therapy</h3>
            <p>Combination hormone therapy may increase the risk of breast cancer. Talk with your doctor about the benefits and 
            risks of hormone therapy.</p>
            
            <h3>Eat a healthy diet</h3>
            <p>Women who eat a Mediterranean diet supplemented with extra-virgin olive oil and mixed nuts might have a reduced 
            risk of breast cancer. The Mediterranean diet focuses on mostly on plant-based foods, such as fruits and vegetables, 
            whole grains, legumes, and nuts. People who follow the Mediterranean diet choose healthy fats, like olive oil, over 
            butter and eat fish instead of red meat.</p>
            
            <h3>Avoid exposure to radiation and environmental pollution</h3>
            <p>Medical-imaging methods, such as computerized tomography, use high doses of radiation. While more studies are 
            needed, some research suggests a link between breast cancer and radiation exposure. Reduce your exposure by having 
            such tests only when absolutely necessary.</p>
            
            <h3>Consider preventive medications if you're at high risk</h3>
            <p>Estrogen-blocking medications, such as selective estrogen receptor modulators and aromatase inhibitors, reduce 
            the risk of breast cancer in women with a high risk of the disease. These medications carry a risk of side effects, 
            so doctors reserve these medications for women who have a very high risk of breast cancer. Discuss the benefits and 
            risks with your doctor.</p>
            """,
            "image_url": "/api/placeholder/600/300"  # Replace with actual image path when available
        }
    ]
    
    # Translate if not English
    if language != "en":
        for article in articles:
            article["title"] = t(article["title"], language)
            article["summary"] = t(article["summary"], language)
            article["content"] = t(article["content"], language)
    
    return articles

def main():
    st.title("Discover")
    st.markdown("### Resources and Articles for Breast Health")
    st.markdown("Explore our collection of informative articles about breast health, cancer awareness, and prevention.")
    
    # Language selection
    # Get language from session state (assuming it's set in the main app)
    language = st.session_state.get('language', 'en')
    
    # Get articles
    articles = get_articles(language)
    
    # Display articles in a grid layout
    col1, col2 = st.columns(2)
    
    for i, article in enumerate(articles):
        if i % 2 == 0:
            with col1:
                create_article_card(
                    article["title"],
                    article["summary"],
                    article["content"],
                    article["image_url"]
                )
        else:
            with col2:
                create_article_card(
                    article["title"],
                    article["summary"],
                    article["content"],
                    article["image_url"]
                )

if __name__ == "__main__":
    # Set page config
    st.set_page_config(
        page_title="Discover - Mammo Mate",
        page_icon="📚",
        layout="wide",
    )
    
    # Initialize session state for language if not already set
    if 'language' not in st.session_state:
        st.session_state['language'] = 'en'
    
    main()