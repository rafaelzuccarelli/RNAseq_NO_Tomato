#################################
# Plot gene ontology enrichment #
#################################

# Requires the package 'ggplot2' (needs to be installed first)
# Load the ggplot2 package
library(ggplot2)
library(plotscale)

# set the working directory where the tables to use are located
args <- commandArgs(trailingOnly=TRUE)

#get the file name and path from terminal 
wd <- getwd()
slash <- '/'
#the paste function join together the working directory (wd) a slash(variable created above) and the csv file name given in terminal
path_file <- paste(wd,slash,args[1],sep= "",collapse=NULL)

# Prepare dataframe
#------------------
# Import the table containing the enriched GO terms by groups
GO_gp <- read.csv(path_file,header=T,stringsAsFactors = T)
input_file_name <- tools::file_path_sans_ext(basename(path_file))
output_file_name <- paste(input_file_name, ".pdf",sep= "",collapse=NULL)
# List objects and their structure contained in the dataframe 'GO_all'

# List objects and their structure contained in the dataframe 'GO_gp'
ls.str(GO_gp)

# Transform the column 'Gene_number' into a numeric variable
GO_gp$Gene_number <- as.numeric(GO_gp$Gene_number)

# Replace all the "_" by a space in the column containing the GO terms
GO_gp$GO <- chartr("_", " ", GO_gp$GO)

# Transform the column 'GO' into factors
GO_gp$GO <- as.factor(GO_gp$GO)

# Transform FDR values by -log10('FDR values')
GO_gp$'|log10(FDR)|' <- -(log10(GO_gp$FDR))

# Change factor order
GO_gp$Group <- factor(GO_gp$Group,levels = c("Bk_Up","Bk_Down"))
GO_gp$GO <- factor(GO_gp$GO,levels=rev(levels(GO_gp$GO)))

# Create a vector with new names for groups to use in the plot
# Replace the terms by your own (\n allow to start a new line)
group.labs <- c(`Bk_Up` = "Bk Up\nregulated",
                `Bk_Down` = "Bk Down\nregulated")

# Draw the plot in facets by group with ggplot2
# to represent -log10(FDR), Number of genes and 
# Fold enrichment of each GO biological process per group (Figure 3)
#-------------------------------------------------------------------
fig2 <- ggplot(GO_gp, aes(x = GO, y = Fold_enrichment)) +
  geom_hline(yintercept = 1, linetype="dashed", 
             color = "azure4", size=.5)+
  geom_point(data=GO_gp,aes(x=GO, y=Fold_enrichment,size = Gene_number, colour = `|log10(FDR)|`), alpha=.7)+
  scale_color_gradient(low="green",high="red",limits=c(0, NA))+
  coord_flip()+
  theme_bw()+
  theme(axis.ticks.length=unit(-0.1, "cm"),
        axis.text.x = element_text(margin=margin(5,5,0,5,"pt")),
        axis.text.y = element_text(margin=margin(5,5,5,5,"pt")),
        axis.text = element_text(color = "black"),
        panel.grid.minor = element_blank(),
        legend.title.align=0.5)+
  xlab("GO")+
  ylab("Fold enrichment")+
  labs(color="-log10(FDR)", size="Number\nof gnenes")+
  facet_wrap(~Group,ncol=2,labeller=as_labeller(group.labs))+#after "ncol=", specify the number of groups you have
  guides(y = guide_axis(order=2),
         colour = guide_colourbar(order=1))

pdf(output_file_name)
fig2
dev.off()


